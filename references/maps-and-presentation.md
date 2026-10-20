# Maps, assets, and presentation

## Maps and collision

Sources: [map settings](https://silversecond.com/WolfRPGEditor/Help/02mapsetting.html), [tileset settings](https://silversecond.com/WolfRPGEditor/Help/02tileset.html).

Verify the map's registered System DB entry, filename, dimensions, tileset, start position, and transfer destinations. Use the editor to register a new map; a file copied onto disk alone is not proof the game's map references resolve. Check destinations against actual bounds and passable tiles.

Tiles have both visual and traversal settings. Passability includes allowed, blocked, behind-character, always-above, and inherit-from-lower-layer behavior; direction restrictions are separate. Counter tiles affect interaction across the counter. Test walking and talking in the runtime rather than judging collision from appearance. Preserve tags when replacing tiles: event logic may use them to identify terrain. A tag of zero is skipped when reading the topmost nonzero tag.

For mapping changes, exercise corners, narrow passages, doors, edges, transfer landings, and overlapping upper layers. Diagnose a blocked route before turning collision off globally.

## Asset geometry

Source: [official material specifications](https://silversecond.com/WolfRPGEditor/Help/06material.html).

Basic tilesets are eight tiles wide, with height divisible by tile size. Documented tile sizes include 16, 32, 40, and 48 pixels; confirm release/project support. Autotile sheets are five tiles high and one or more animation columns wide.

Walking sheets depend on configured three/five animation patterns and four/eight directions. Match the actual project; do not apply RPG Maker sheet conventions. A single character-frame width must be even. Filename suffixes affect interpretation: `T.png` adds a stopped frame, `TX.png` adds stopped animation, and `$.png` displays the whole image unsplit. Preserve meaningful suffixes during renaming.

Prefer full-color alpha PNG for transparent art. Check rendering in-game if the editor preview looks wrong. OGG is the manual's recommended stable audio format; some WAV/MP3 encodings depend on system codecs, and 24-bit WAV can cause failures. Do not replace working sound merely to standardize formats.

For art integration, inspect dimensions, transparency, palette/scaling behavior, and per-frame alignment before replacing files. Keep an original and compare the final runtime appearance. Geometry checks do not prove correct animation direction ordering; compare against a working local sheet and inspect each direction.

## Text and picture ownership

Source: [special characters](https://silversecond.com/WolfRPGEditor/Help/06specialword.html).

Text escapes are case-sensitive and use half-width characters. Common forms:

| Form | Purpose |
| --- | --- |
| `\v[N]`, `\s[N]` | Normal numeric/string variable substitution |
| `\self[N]`, `\cself[N]` | Current event/common self value |
| `\udb[T:D:F]`, `\cdb[T:D:F]`, `\sdb[T:D:F]` | Database substitution |
| `\f[N]`, `\c[N]` | Font size / configured color |
| `\!`, `\.` | Input pause / quarter-second pause |
| `\^` | Finish without waiting for input |
| `\\` | Literal backslash |

Preserve control codes and placeholders when editing dialogue. Match source text exactly unless wording changes were requested. Older releases may differ in nested-substitution rules; avoid adding complicated nesting without a local test.

For HUDs, portraits, and custom menus, first inspect the game's picture ID allocations and coordinate conventions. Record which event owns each new ID and when it is erased. Test opening, closing, cancellation, transfer, and save/load paths so stale pictures and locks do not remain. Keep UI design distinct from engine-ready event implementation until imported and tested.

Asset permissions are independent of image compatibility. Keep source/license information for supplied resources; the ability to load an RPG Maker asset does not establish permission to use it in WOLF.
