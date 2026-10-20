# WOLF RPG Editor skill for Codex

## About This Project

I love indie games, indie creators, and building useful tools for niche spaces. My work as a developer is fueled by a deep appreciation for tabletop RPGs, Japanese niche media, and everything from *Cave Story* to *Baldur's Gate 3*.

While I’m currently building both a CRPG and a JRPG in Godot, niche engines are just infinitely more fun. I put this Codex skill together using Codex to bridge the gap for developers who want to build games in **WOLF RPG Editor** without having to wade through the specific minutiae of Japanese RPG engines.

If you're into niche game dev and retro toolchains, I hope this makes your creation process smoother and more accessible!

## Overview

A portable skill for creating, inspecting, editing, and debugging WOLF RPG Editor / Woditor games. It combines original task-oriented instructions, offline references, version-scoped identifier tables, and two dependency-free Python helpers.

## Install and use

Copy this entire folder as `wolf-rpg-editor` into a Codex skill directory, for example `~/.codex/skills/`. Keep the relative structure intact. Invoke it with `$wolf-rpg-editor` and the target project path.

```text
Use $wolf-rpg-editor to inspect my project, identify its engine and Basic System,
and implement a two-page chest that grants its reward once and stays open after save/load.
```

Start with [SKILL.md](SKILL.md). It routes tasks to focused references. Search the included knowledge without network access:

```text
python scripts/lookup.py "save load"
python scripts/lookup.py "Sys143"
python scripts/lookup.py "Change Items"
```

## Included

- Project preservation, native text exchange, map/common-event design, variables, databases, assets, debugging, and export workflows.
- Operational guidance across the principal event-command families and advanced behavior pitfalls.
- A 3.691 native-text profile tested with actual editor export/import/readback.
- Searchable system labels, common-event interfaces, and database schema labels from a version-scoped sample.
- A source list with authors/credits and a 77-response official-manual research catalogue, including unavailable/wrapper status.
- Read-only project inventory and change comparison.

Python helpers require Python 3.10+ and no installed packages. WOLF RPG Editor/runtime and any desktop control are separate. No network, account, API key, or MCP server is required by this skill. Engine-backed work needs a compatible local engine.

## Validation and limits

See [VALIDATION.md](VALIDATION.md). The package was relocated and read offline, its helper behavior checked against fixtures, and its native text route tested with WOLF 3.691 on a disposable installation copy. Gameplay, GUI interactions, save compatibility, and Pro-only operations were not tested.

This is a substantial authoring reference, not a complete implementation of every WOLF feature or a binary file serializer. Version-scoped sample IDs must be checked against each actual game. It does not include engine executables, DLLs, game media, full sample-game exports, downloaded manuals, or raw website snapshots.

## Sources and credits

The canonical [sources and credits](references/sources.md) identify the four requested documentation sites, original authors, English translation contributors, and local verification material. The [research catalogue](references/source-catalog.md) lists inspected/fetched official URLs; its [JSON companion](references/source-catalog.json) records retrieval times and source hashes. Downloaded pages were research inputs, and are not included as a copied manual.

WOLF RPG Editor is created by SmokingWOLF / SilverSecond. English translation credit: translation by Yumu, edited by Anya and Lolo. Sample-data translation by Yumu. This project is an independent Codex skill and is not an official WOLF distribution.

## Git contents

This folder is the repository-ready payload. Version `SKILL.md`, `README.md`, `VALIDATION.md`, `.gitignore`, `agents/`, `references/`, `scripts/`, and `tests/`. Keep engine installations, game projects, saves, downloaded source pages, temporary probes, local paths, and credentials outside the repository. No remote repository has been created or pushed by this build.
