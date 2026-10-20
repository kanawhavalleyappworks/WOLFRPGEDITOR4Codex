# Project workflow

## Recognize the layout

Source: [official file guide](https://silversecond.com/WolfRPGEditor/Help/01filelist.html), inspected 2026-10-20.

The conventional project has `Editor.exe` and `Game.exe` beside `Data/`. `Data/BasicData/` holds core settings, databases, common events, and tileset settings; `Game.dat` contains game settings. `Editor.ini` holds editor preferences, including last-opened map information. `Game.ini` holds runtime preferences. `Config.exe` exposes runtime configuration. Map files use `.mps`; actual subfolder names should be discovered from the project.

An executable with `Data.wolf` or folder archives may be a distribution rather than editable source. Ask for source data when authoring requires it; archive presence alone does not establish that editable files are absent. Do not rename `Data` casually. Current releases have explicit alternate-folder options; inspect launch arguments if the conventional tree seems missing.

## Inspect without mutation

`scripts/project_inventory.py` uses Python 3.10+ standard library only. It never executes the game, opens binaries through a decoder, follows directory links/reparse points, or writes into the scanned tree. It reports relative file paths, sizes, timestamps, conventional markers, map candidates, archives, and errors. `--hash` adds SHA-256 for change comparison. Reports can expose project filenames; keep them local unless sharing is requested.

```text
python "<skill>/scripts/project_inventory.py" scan "<project>" --hash > "<outside-project>/before.json"
python "<skill>/scripts/project_inventory.py" scan "<project>" --hash > "<outside-project>/after.json"
python "<skill>/scripts/project_inventory.py" diff "<outside-project>/before.json" "<outside-project>/after.json"
```

Both manifests must be complete hashed scans. A nonzero scan exit means inspection was incomplete. Diff returns 0 for no unapproved byte changes, 1 for changes outside supplied allow patterns, and 2 for invalid/incomplete input. `--allow "Data/MapData/Town.mps"` may be repeated to allow intended changes; all changes remain visible in the report. Patterns use forward slashes and case-sensitive matching; `*` can span subdirectories. Avoid broad allow patterns. Timestamp-only differences are not byte changes.

For custom launch layout:

```text
python "<skill>/scripts/project_inventory.py" scan "<project>" --data-dir Data3 --basic-dir BasicD2 --hash
```

Both paths must be relative and inside their respective parent: data under project, basic under data. The helper does not infer launch settings or read version resources. Layout warnings are observations, not corruption diagnoses.

## Work on a recoverable copy

Before import, preserve a complete project copy with engine binaries, source data, assets, and relevant saves. Record engine/edition/language and the intended edit scope. Close the editor before externally replacing files so stale in-memory data cannot overwrite the change. Keep baselines outside the project; otherwise scans and distribution export may pick them up.

After editing, compare byte hashes and examine unexpected changes. Editor preferences, backups, and runtime saves may change legitimately, but account for them. Promote only the tested changed files with their dependencies, retain rollback data, and reopen in the matching editor.
