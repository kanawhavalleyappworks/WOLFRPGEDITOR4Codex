#!/usr/bin/env python3
"""Read-only project inventory and byte-change comparison; Python 3.10+."""

import argparse
import fnmatch
import hashlib
import json
import os
from pathlib import Path
import stat
import sys


def relative_child(parent, value):
    candidate = parent / value
    if Path(value).is_absolute() or ".." in Path(value).parts:
        raise ValueError("Layout paths must be relative without '..'")
    candidate.resolve().relative_to(parent.resolve())
    return candidate


def linked(info):
    return stat.S_ISLNK(info.st_mode) or bool(
        getattr(info, "st_file_attributes", 0) & 0x400
    )


def sha256(path):
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def scan(args):
    root = Path(args.root).resolve(strict=True)
    if not root.is_dir():
        raise ValueError("Project root must be a directory")
    data = relative_child(root, args.data_dir)
    basic = relative_child(data, args.basic_dir)
    files, skipped, errors = [], [], []

    def walk(directory):
        try:
            with os.scandir(directory) as stream:
                entries = sorted(stream, key=lambda item: item.name)
        except OSError as exc:
            errors.append({"path": directory.relative_to(root).as_posix(), "error": str(exc)})
            return
        for entry in entries:
            path = Path(entry.path)
            rel = path.relative_to(root).as_posix()
            try:
                before = path.lstat()
                if linked(before):
                    skipped.append(rel)
                elif stat.S_ISDIR(before.st_mode):
                    walk(path)
                elif stat.S_ISREG(before.st_mode):
                    record = {"path": rel, "size": before.st_size, "mtime_ns": before.st_mtime_ns}
                    if args.hash:
                        record["sha256"] = sha256(path)
                    after = path.lstat()
                    if (before.st_size, before.st_mtime_ns, before.st_ino) != (
                        after.st_size, after.st_mtime_ns, after.st_ino
                    ) or linked(after):
                        errors.append({"path": rel, "error": "File changed during scan; repeat while idle"})
                    files.append(record)
                else:
                    skipped.append(rel)
            except OSError as exc:
                errors.append({"path": rel, "error": str(exc)})

    walk(root)
    names = {record["path"] for record in files}
    def marker(name):
        return any(Path(value).name.casefold() == name.casefold() and "/" not in value for value in names)

    basic_prefix = basic.relative_to(root).as_posix().rstrip("/") + "/"
    warnings = []
    if not any(value.startswith(basic_prefix) for value in names):
        warnings.append("No regular files found in selected basic-data directory; inspect layout or source availability")
    if not marker("Editor.exe") and not marker("EditorPro.exe"):
        warnings.append("No conventional editor executable at root; version and editing capability unknown")
    result = {
        "schema": 1, "root": str(root), "hashed": args.hash,
        "complete": not errors and not skipped,
        "layout": {"data": data.relative_to(root).as_posix(), "basic": basic.relative_to(root).as_posix()},
        "markers": {name: marker(name) for name in ("Editor.exe", "EditorPro.exe", "Game.exe", "GamePro.exe", "Data.wolf")},
        "maps": sorted(value for value in names if value.lower().endswith(".mps")),
        "archives": sorted(value for value in names if value.lower().endswith(".wolf")),
        "files": files, "skipped": skipped, "errors": errors, "warnings": warnings,
        "limits": "No version detection, binary parsing, reference resolution, or engine validation",
    }
    emit(result)
    return 0 if result["complete"] else 2


def load_manifest(path):
    # utf-8-sig and UTF-16 cover common PowerShell stdout redirection encodings.
    raw = Path(path).read_bytes()
    text = raw.decode("utf-16" if raw.startswith((b"\xff\xfe", b"\xfe\xff")) else "utf-8-sig")
    value = json.loads(text)
    if not isinstance(value, dict) or value.get("schema") != 1 or value.get("hashed") is not True or value.get("complete") is not True:
        raise ValueError("Comparison requires complete schema-1 scans with --hash")
    records = {}
    for item in value["files"]:
        if not isinstance(item, dict):
            raise ValueError("Manifest file records must be objects")
        name, digest = item["path"], item["sha256"]
        if name in records or not isinstance(digest, str) or len(digest) != 64:
            raise ValueError("Duplicate path or invalid hash in manifest")
        int(digest, 16)
        records[name] = item
    return value, records


def diff(args):
    before_meta, before = load_manifest(args.before)
    after_meta, after = load_manifest(args.after)
    if before_meta["layout"] != after_meta["layout"]:
        raise ValueError("Cannot compare manifests with different selected layouts")
    changes = []
    for name in sorted(before.keys() | after.keys()):
        if name not in before:
            kind = "added"
        elif name not in after:
            kind = "removed"
        elif before[name]["sha256"] != after[name]["sha256"]:
            kind = "modified"
        else:
            continue
        changes.append({"path": name, "kind": kind,
                        "allowed": any(fnmatch.fnmatchcase(name, pattern) for pattern in args.allow)})
    unexpected = sum(not item["allowed"] for item in changes)
    emit({"changes": changes, "unexpected_count": unexpected,
          "same_root": before_meta["root"] == after_meta["root"],
          "limits": "Byte changes only; allowed does not mean correct or engine-tested"})
    return 1 if unexpected else 0


def emit(value):
    print(json.dumps(value, ensure_ascii=True, indent=2))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    inspect = sub.add_parser("scan", help="Read project files without executing or modifying them")
    inspect.add_argument("root")
    inspect.add_argument("--hash", action="store_true", help="Hash every regular file for byte comparison")
    inspect.add_argument("--data-dir", default="Data")
    inspect.add_argument("--basic-dir", default="BasicData")
    inspect.set_defaults(run=scan)
    compare = sub.add_parser("diff", help="Compare complete hashed scans, including different project copies")
    compare.add_argument("before")
    compare.add_argument("after")
    compare.add_argument("--allow", action="append", default=[], help="Allowed case-sensitive forward-slash path glob (repeatable)")
    compare.set_defaults(run=diff)
    args = parser.parse_args()
    try:
        return args.run(args)
    except (OSError, ValueError, KeyError, TypeError) as exc:
        emit({"error": str(exc)})
        return 2


if __name__ == "__main__":
    sys.exit(main())
