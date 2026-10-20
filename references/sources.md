# Provenance and coverage

Reviewed 2026-10-20. The bundled notes are newly written operational summaries and workflows, not a copied manual or screenshot archive. They can be used offline. Links below are provenance and optional refresh targets; following them is not required to use the local notes. No engine or third-party game assets are redistributed.

## Authority and version handling

1. The matching installed editor, its own help, and observed export/readback behavior establish what that project can use.
2. SmokingWOLF's official manual documents engine semantics. Its live pages contain later version annotations beyond the landing page's main update log. Do not treat that log as an exact ceiling on all features.
3. The Perfect Guide explains practical workflows and the Basic System. Sample event numbers and DB layouts are tied to its examples/generations.
4. English translations help resolve terminology; their feature coverage may lag. A translation is not evidence that the same feature exists in every English binary.

Do not auto-upgrade a project or fetch executable tools to compensate for missing features. Use the local supported route, then report any genuinely missing capability.

## User-supplied source entrypoints

| Source | Status and use |
| --- | --- |
| [Official Perfect Guide](https://silversecond.com/WolfRPGEditor/Guide/) | Landing page uses frames; individual articles below were accessible. Practical examples, not a full locally mirrored guide. |
| [Official manual](https://silversecond.com/WolfRPGEditor/Help/) | Primary technical source. Copyright SmokingWOLF; landing page permits quoting its text for explanations. Local notes use concise paraphrases. |
| [Anya & Lolo English guide](https://anya-and-lolo.github.io/wolf-rpg-editor/guide/index.html) | Landing page says the original guide used 2.x and lists many sections as forthcoming. Variable and common-event articles inspected; original author credits preserved where used. |
| [Dreamsavior manual](https://dreamsavior.net/docs/wolf-rpg-editor-manual/) | Index inspected; exposes translated FAQ, resources, special characters, and translation topics. No detailed technical claim in these notes relies solely on the index. Its root URL without a trailing slash initially failed to fetch. |

## Technical source map

| Local topic | Primary inspected pages |
| --- | --- |
| Project layout | [Files and INI](https://silversecond.com/WolfRPGEditor/Help/01filelist.html) |
| Editor text exchange and old-language import | [Editor options](https://silversecond.com/WolfRPGEditor/Help/02editor_option.html) |
| Text CLI and test launching | [Controls and arguments](https://silversecond.com/WolfRPGEditor/Help/01control.html) |
| Event code, page priority, triggers | [Event window details](https://silversecond.com/WolfRPGEditor/Help/04eventwindowB.html), [creating events](https://silversecond.com/WolfRPGEditor/Help/04eventmain.html) |
| Common event parameters and scheduling | [Settings](https://silversecond.com/WolfRPGEditor/Help/02commonev.html), [calls](https://silversecond.com/WolfRPGEditor/Help/04ev_common.html) |
| Variables | [Notation and arithmetic](https://silversecond.com/WolfRPGEditor/Help/04ev_calc.html), [numeric references](https://silversecond.com/WolfRPGEditor/Help/06valueget.html), [English naming tutorial](https://anya-and-lolo.github.io/wolf-rpg-editor/guide/working-with-variables.html) |
| DBs and saved schema | [Database overview](https://silversecond.com/WolfRPGEditor/Help/05database.html), [DB commands](https://silversecond.com/WolfRPGEditor/Help/04ev_db.html) |
| RPG system boundary | [Basic System](https://silversecond.com/WolfRPGEditor/Guide/BASE_001.html), SmokingWOLF |
| Persistent event recipe | [Chest](https://silversecond.com/WolfRPGEditor/Guide/EV_006.html), ミケ |
| Maps, collision | [Map settings](https://silversecond.com/WolfRPGEditor/Help/02mapsetting.html), [tilesets](https://silversecond.com/WolfRPGEditor/Help/02tileset.html) |
| Art and sound | [Material specifications](https://silversecond.com/WolfRPGEditor/Help/06material.html) |
| Message codes | [Special characters](https://silversecond.com/WolfRPGEditor/Help/06specialword.html) |
| Debugging and export | [Debug tools](https://silversecond.com/WolfRPGEditor/Help/01debug.html), [game-data creation](https://silversecond.com/WolfRPGEditor/Help/02gamemake.html) |

## Extending coverage

This is a substantial authoring/diagnostics reference with command-family guidance and version-scoped local indexes. Complete binary formats, every advanced effect's parameter schema, full semantics for every system value, and all Basic System generations are not bundled. For an uncovered task, first inspect matching local help or a small native export. If online research is needed and available, add only verified, useful notes with source URL, author, date, version scope, and uncertainty. Do not turn unverified community workarounds into universal rules.

When refreshing, compare the specific page and installed version. Preserve working offline notes until replacements are verified; URLs alone do not replace local instructions.

## Complete research URL inventory

The [official manual catalogue](source-catalog.md) lists all 77 HTML responses fetched during research, including wrappers and two soft-404 pages. [Machine-readable provenance](source-catalog.json) records URLs, original titles, authorship, retrieval timestamps, content hashes, and research status. A fetched page is not a claim that every paragraph was independently validated or bundled. The original HTML, extracted research text, images, and scripts are not distributed.

Additional command sources are linked next to their guidance in [command reference](command-reference.md) and [advanced operations](advanced-operations.md). Current official pages are primary technical sources; the external English materials supply translation context and introductory explanations.

## Translation package and locally verified sources

- [WoditorTranslationGallery](https://github.com/WoditorTrans2000/WoditorTranslationGallery): upstream translation project named by the installed package README; used to identify package provenance, not to replace the installed binaries during testing.
- [Yumu's sample-data translations](https://github.com/yumunet/WoditorDataTranslations): upstream source identified by the installed README for sample-game and extra-content translations.
- [Anya and Lolo](https://github.com/Anya-and-Lolo): English editor translation editors and guide contributors.
- Installed `READ ME.txt`: identifies Editor 3.691, Sample Game 3.6, `Editor.Lang.dll`, translation credits, and the legacy 2.24Z PDF limitation.
- Installed `Sample Game Manual.txt`: controls and sample/Basic System context. The PDF was not used as a current 3.691 specification.
- Installed `Editor.Lang.SystemValue.txt` and `Editor.Lang.SystemString.txt`: UTF-16 label tables used for the [system index](system-index-3.691.md); original file hashes appear in that reference. Labels and flags are retained; the package does not contain the original DLL.
- A native export from a disposable copy of the sample: used for [common-event/type lookup](sample-system-3.691.md), [schema labels](sample-database-schema-3.691.md), and the [native-text profile](native-text-3.691.md). Full event bodies, data records, and media are not bundled.
- Local file-version resources: Editor.exe and Game.exe both reported `3.691.2026.408`. Engine binaries were neither modified in place nor included in the package.

The [verification profile](verification-profile.json) records engine hashes and unedited native-export hashes without embedding the executable or game source files.

English credit retained from the installed package: en-US translation by [Yumu](https://github.com/yumunet), edited by [Anya and Lolo](https://github.com/Anya-and-Lolo). Sample Game 3.6, Graphic Maker, and Version 1 asset translations by Yumu. Original WOLF RPG Editor and Basic System copyright belongs to SmokingWOLF / SilverSecond. The chest tutorial credits ミケ; the English variable tutorial credits Kijiko.

## Distribution boundaries

This repository contains original instructions/helpers and limited factual identifier/schema-label tables with attribution. It does not relicense WOLF RPG Editor, its translation binaries, third-party website content, or sample-game media. Source URLs and credits document provenance; they do not replace the original materials' own terms. No full downloaded manual or engine is needed to read the included operational notes.
