# Advanced operations and engine pitfalls

## Scheduling and initialization

[Official implicit behavior](https://silversecond.com/WolfRPGEditor/Help/01specifi.html).

The documented evaluation sequence is parallel map events, automatic/contact map events, automatic common events, parallel common events, then eligible player movement/confirm activation. Within a group, lower event IDs are checked first. This explains why a Basic System initializer in a parallel common event may need a frame before a map's startup logic uses its values.

Parallel cancellation is not an atomic boundary: optimized non-waiting commands can continue until an interruptible point. Explicitly end the event after changing its own eligibility if later commands must not run. A waiting transition can pause parallel events too. Command-count errors include weighted expensive operations, so the reported count is not a literal count of visible lines.

For a new shared service, define its initialization point, readiness state, owner, shutdown behavior, and behavior after load. A short wait copied blindly into every event is not a substitute for finding the real dependency.

## Picture layers, timing, and effects

Sources: [Picture](https://silversecond.com/WolfRPGEditor/Help/04ev_picture.html), [Effect](https://silversecond.com/WolfRPGEditor/Help/04ev_effect.html).

Picture IDs ≥100000 draw above message/choice windows; ordinary 0–99999 pictures draw below them. Negative IDs cross engine layer bands. With picture behavior v2 (documented from 3.50), bands below zero divide fog, upper tiles, characters, base tiles, and panorama at -100000 intervals. Behavior v1 has fewer boundaries. Inspect `PICTURE_DRAW_VERSION` in a native settings export and the actual runtime result before allocating negative picture IDs.

Z-order adjusts ordering within the relevant engine layer group; it does not make every picture freely cross engine layer boundaries. Character picture links add rendering state separate from ordinary picture coordinates. Map-event links end on transfer; leader/follower links can survive. Do not also scroll-link a picture already linked to a character.

Use a small scene with one foreground tile, one character, one message, and the candidate picture when validating a custom layering system. Avoid declaring success from a screenshot that lacks the actual overlapping elements.

## Coordinate and unit ledger

Record these values with each subsystem rather than silently converting them:

| Quantity | Required interpretation |
| --- | --- |
| Map position | Tile/half-tile/precise coordinate selected by the command |
| Sprite position | Logical movement/collision position versus rendered offset |
| Picture X/Y | Pixels relative to its origin and link mode |
| Picture angle | Tenths of a degree where documented |
| Timing | Game frames and configured FPS |
| Audio position | Milliseconds except documented MIDI tick paths |
| Opacity | Usually 0–255 in picture parameters |
| Color | RGB correction percentages versus actual 0–255 channel values |

Test a one-unit change to establish direction and scale. Do not apply a render-effect transform twice because an engine query returns the untransformed position.

## Hidden string-code tools

[Official hidden-code page](https://silversecond.com/WolfRPGEditor/Help/04ev_string_specialcode.html).

These execute through the String command's hidden-code mode; they are not normal message escapes. Useful families include file/directory existence, string width/byte/line slicing, event ID/name lookup, image dimensions/ARGB sampling, conversion to/from XY image planes, sound duration, Windows speech, and pathfinding. Check release support and the exact return representation before using a result as a number or filename.

Examples of documented forms:

```text
<<GET_FILE_EXIST>>Data/Picture/example.png
<<GET_IMAGE_SIZE>>Picture/example.png
<<GET_MAPEVENT_NAME_FROM_ID>>0
<<GET_COMMONEVENT_ID_FROM_NAME>>Unique Event Name
<<GET_SOUNDTIME>>Data/BGM/example.ogg
```

Path bases vary even in these examples: file existence/sound-time include `Data/`, image-size does not. Do not normalize every hidden-code path under one rule. These are syntax examples from the manual, not engine-tested fixtures in this package. When adding an uncovered hidden operation, derive a minimal native example and record its result/failure sentinel.

## Settings and compatibility

Sources: [game settings](https://silversecond.com/WolfRPGEditor/Help/02gamesetting.html), [behavior adjustment](https://silversecond.com/WolfRPGEditor/Help/02ver_ajust.html).

Editor version, runtime version, and configured runtime-behavior version are separate facts. An upgraded executable may retain older compatibility settings. Record tile size, logical screen size, display multiplier, FPS, character direction/pattern settings, movement unit, picture behavior, font, and compatibility mode before altering presentation or timing.

Preserve a project's working mode during a focused feature pass. A deliberate migration should use a copied project, one compatibility change at a time, targeted comparisons, and existing saves. A compatibility selector is not proof every old/new difference is covered. Older manual sections can conflict with later version annotations; use the paragraph tied to the feature/version and native readback rather than the oldest general sentence on the page.

## Database schema and runtime names

Sources: [type definition](https://silversecond.com/WolfRPGEditor/Help/05dbtype.html), [Variable DB](https://silversecond.com/WolfRPGEditor/Help/05changedb.html).

Field input widgets can be numeric, string, database-reference selectors, file selectors, or custom choices. The widget stores a value; its friendly label is not necessarily the stored string. Data names may be manually assigned, sourced from the first string field, inherited from another type, or referenced from another DB. Determine that mode before renaming records.

Append new Variable DB types and fields at the end for save evolution. Adding a field still needs a migration/default policy: a loaded old save may receive an empty string or default numeric value, which can be valid structurally and wrong for gameplay. Preserve stable IDs independently of display names.

## System DB map

[Official type descriptions](https://silversecond.com/WolfRPGEditor/Help/05systemtype.html).

| Type | Role |
| --- | --- |
| 0 | Registered maps and map audio/loop settings |
| 1–3 | BGM, BGS, SE lists |
| 4 | String-variable names |
| 5–6 | System string/value names |
| 7 | Stored transfer destinations |
| 8–9 | Character/character-shadow graphics |
| 10 | Message pause/choice window/cursor graphics |
| 11 | Transition images |
| 12 | Text colors |
| 13 | Panorama/fog images and scrolling |
| 14 | Normal-variable names |
| 15–23 | Spare-variable banks |
| 24 | Portrait names/files for project presentation logic |

Treat this as an engine-oriented locator, then verify actual fields in the matching export. Portrait registration alone does not implement portrait display. A stored asset path is generally relative to the game's data context, not the repository or skill folder.
