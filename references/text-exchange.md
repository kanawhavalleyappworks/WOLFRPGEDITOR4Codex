# Native text and event exchange

## Capability and baseline

Sources: [editor options](https://silversecond.com/WolfRPGEditor/Help/02editor_option.html), [launch options](https://silversecond.com/WolfRPGEditor/Help/01control.html), [event window](https://silversecond.com/WolfRPGEditor/Help/04eventwindowB.html), [common-event settings](https://silversecond.com/WolfRPGEditor/Help/02commonev.html). Inspected 2026-10-20. These are current Japanese manual features; availability in older/translated releases must be demonstrated locally.

Use the installed editor's exported sample as the schema. This package intentionally contains no fabricated full-project text syntax or binary decoder.

## Automatic text files

The editor-options text-export setting emits `*.Auto.txt` when saving settings, databases, maps, common events, and tilesets. These are editor exchange files; the runtime does not execute them. The options window also has bulk export/import actions for basic data and maps. Basic exports go under `BasicData`; map exports reproduce the folder structure under `Data`. Import reconstructs game data and can overwrite it.

Legacy files created before version 3 use language-dependent encoding. The old-file language setting affects imported common events, tilesets, DB data, and maps. Do not force UTF-8 onto an older project merely because new releases use it. Preserve observed encoding, line endings, delimiters, escapes, and field types. A successful decode with no exception does not prove the encoding is right; inspect representative Japanese and accented text.

## Command-line route in supporting releases

Run from the copied project's editor directory, using that project's matching executable:

```text
Editor.exe -txtoutput -txt_folder SkillBaseline -target ALL
Editor.exe -txtinput -txt_folder SkillBaseline -target ALL
```

`-target` accepts `ALL`, `BASIC`, or `MAP`. The text folder is relative to `Editor.exe`; default is `Data_AutoTXT`. Optional `-wait` leaves a keypress prompt. `-f` selects an alternate data folder; `-basic` selects an alternate basic-data folder. Keep export/import selections consistent. Text import is a write operation; a headless launch or zero exit status alone does not prove correctness.

First export a baseline from a disposable copy, import it without edits, reopen, and re-export to a second location. Investigate structural differences and text loss before proceeding. Then make the smallest edit and import it into another recoverable copy. Read back the affected commands/pages/DB fields and playtest. If import scope is broad, ensure the export includes every file that scope can overwrite. Never point import at a partial folder without understanding its missing-file behavior in that release.

## Clipboard event code

In documented releases, `Ctrl+Shift+C` copies display text; `Ctrl+Alt+C` copies event code; `Ctrl+Alt+V` pastes event code. Focus must be in the event command list. Importable blocks have `WoditorEvCOMMAND_START` and `WoditorEvCOMMAND_END` sentinels. Preserve exact leading/trailing whitespace rules and parameter structure emitted by the editor. A prose command list is not pasteable code. Do not deduce opcodes or quote escaping from appearance alone; make a small sample in the matching editor and export it.

## Common-event files

Native common-event export/import supports `.common` and text routes in documented versions. Loading can replace events at the destination, including multiple events from one export. Select deliberately unused slots and inventory referenced DBs, variables, picture ranges, assets, and other events first. Recheck call targets after importing. Calling a `.common` file directly at runtime is an obsolete feature, unsupported since version 2.00; import it and call the installed event.
