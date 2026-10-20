# Native text exchange verified with 3.691

## Observed installation

Checked 2026-10-20 against the user's existing English translation package. Both executable file versions reported `3.691.2026.408`; the package README identifies Editor 3.691, Sample Game 3.6, and a legacy 2.24Z PDF that omits newer features. Translation files are loaded through `Editor.Lang.dll`; preserve it and the package's editor/font configuration when copying this installation. This is a tested version profile, not a requirement to use this exact release.

Credits: WOLF RPG Editor and original Basic System by SmokingWOLF. English editor translation by Yumu, edited by Anya and Lolo; sample-data translation by Yumu. See [sources](sources.md) for upstream links. No executable, DLL, full sample game, or manual PDF is included in this skill.

## Engine-backed checks

A complete disposable copy of the installation was used. Native ALL export emitted ten files: six basic-data files and four maps. A no-edit ALL import followed by re-export produced identical paths and SHA-256 hashes for all ten text files.

A second probe changed only `GAME_TITLE_MAIN` in the copied settings export, imported BASIC, and exported ALL. Only `BasicData/Game.dat.Auto.txt` changed, and its bytes differed only by the intended title replacement. This establishes this setting's native import/readback behavior. It does not establish runtime display, event-code import, gameplay, or save compatibility.

## Export tree

```text
<chosen text folder>/
  BasicData/
    Game.dat.Auto.txt
    CommonEvent.dat.Auto.txt
    DataBase.Auto.txt
    CDataBase.Auto.txt
    SysDataBase.Auto.txt
    TileSetData.dat.Auto.txt
  MapData/
    TitleMap.mps.Auto.txt
    SampleMapA.mps.Auto.txt
    SampleMapB.mps.Auto.txt
    Dungeon.mps.Auto.txt
```

Database text exports omit `.dat`/`.project` in their names. Do not construct names by appending `.Auto.txt` to every input binary. The inspected settings output uses UTF-8 without BOM and CRLF; preserve each file's observed bytes outside the edit rather than relying on a default text writer.

## Recognizable headers

These are identification fragments, not complete importable files:

```text
[GAMESETTING_TEXT_OUTPUT]
GAME_TITLE_MAIN=Example Title
```

```text
[COMMON_EVENT_TEXT_OUTPUT]
COMMON_EVENT_NUM=225
--------------------------
COMMON_ID=0
COMMON_NAME=...
VALINPUT_NUM=3
STRINPUT_NUM=0
```

```text
[DATABASE_TEXT_OUTPUT]
TYPE_NUM=18
----
TYPE_ID=0
ITEM_NUM=37
DATATYPE_0=2000
```

```text
[MAPDATA_TEXT_OUTPUT]
MAP_WIDTH=20
MAP_HEIGHT=15
MAPLAYER=3
[--MAP_START--]
```

Map files also contain an `[EVENTDATA_TEXT_OUTPUT]` section after tile-layer data. Preserve both parts. Serialized event page indices and displayed editor page numbers can differ: do not apply a universal ±1 adjustment without a generated comparison. Numeric datatype/trigger codes above are observed values, not a promised complete enum mapping.

## Making a narrow edit

Export the whole selected scope to a new folder. Make a baseline no-edit round trip first. For a simple scalar setting, replace one exact key/value byte sequence and assert the match count is one. Keep filenames, section markers, counts, and encoding intact. Import into a disposable copy; export again to a different folder; compare every file in the scope and the exact changed content. Never use this key/value strategy inside serialized commands without accounting for their own quoting/nesting rules.

The [sample system index](sample-system-3.691.md) identifies observed common-event entry points and DB types, but a different game's export remains authoritative. The [system variable index](system-index-3.691.md) preserves the translated numeric labels and flags for lookup.
