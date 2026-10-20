# State, variables, and RPG data

## Scope and types

Sources: [variable notation](https://silversecond.com/WolfRPGEditor/Help/04ev_calc.html), [English variable guide](https://anya-and-lolo.github.io/wolf-rpg-editor/guide/working-with-variables.html), author Kijiko, English edition Anya & Lolo.

| Notation | Meaning |
| --- | --- |
| `Vn` | Normal numeric variable |
| `Vn-j` | Spare numeric variable notation |
| `Sn` | String variable |
| `Selfn` | Map-event local numeric state |
| `CSelfn` | Common-event state; 5–9 are strings, other slots numeric |
| `Sysn`, `SysSn` | System numeric/string values; inspect their documented meaning and writeability |

Name new variables and search uses before reusing a slot. A common event's self variables are not a substitute for map-event state or a guarantee of recursion-safe local storage. Define explicit initialization and result handling for reusable events.

Optimized common-event arithmetic can overflow near signed 32-bit limits. Keep calculations within a deliberately bounded range and test intermediate products. Do not silently assume floating-point arithmetic or language-library division behavior.

## Literal values versus references

Source: [numeric reference values](https://silversecond.com/WolfRPGEditor/Help/06valueget.html).

Numeric fields that support variable-call values interpret large numbers as references. Constants occupy -999999 through 999999; check the specific command before treating a larger number as a literal.

| Encoded value | Reference |
| --- | --- |
| `1100000 + X` | Current map event Self X |
| `1600000 + X` | Current common event CSelf X |
| `2000000 + X` | Normal variable X |
| `3000000 + X` | String variable X |
| `9000000 + X` | System numeric variable X |
| `9900000 + X` | System string X |

For example, 2000012 refers to V12 in a reference-aware field; it is not the quantity two million and twelve. Prefer the editor's named selectors where possible. Message substitutions such as `\v[12]` are a different mechanism and are not arithmetic expressions.

## Database contracts

Sources: [database overview](https://silversecond.com/WolfRPGEditor/Help/05database.html), [DB commands](https://silversecond.com/WolfRPGEditor/Help/04ev_db.html).

System DB holds engine-defined structures. User DB generally stores static design data; Variable DB stores runtime-changing state. Each address includes database kind, type, data entry, and field. Read field names, types, and project conventions before editing; identical numbers in different databases identify different data.

Do not reorder referenced entries or insert/remove numbered types to make a list look tidy. Changing a System DB type schema can break engine assumptions. Existing saves preserve Variable DB field types: switching a numeric field to string or the reverse can disagree with saved state. Append-only extensions are supported by the documented database behavior, but still need initialization and existing-save tests; this is not blanket proof of compatibility.

DB commands can select transfer direction between DB and variables. Verify the source/destination direction, numeric/string type, valid bounds, and actual target address. Do not overwrite a DB value when intending to read it. XY arrays are separate numeric two-dimensional structures; do not treat them as ordinary DB reference addresses.

## Basic System customization

Source: [what the Basic System provides](https://silversecond.com/WolfRPGEditor/Guide/BASE_001.html), SmokingWOLF.

The Basic System implements RPG behavior using common events and databases: party, items, money, skills, battles, shops, menu, messages, and save/load UI. These are project data rather than universally built-in event opcodes. The sample title flow is implemented separately with map events. Removing sample maps is different from removing the RPG system.

For items, equipment, enemies, skills, battle hooks, or menus: locate the current project's data schema and public common events; inspect a working example; duplicate/adapt it into unused IDs; update the relevant references; exercise the result through gameplay. Do not copy tutorial common-event IDs across Basic System generations or assume a custom game retained the sample schema.

For a blank-system project, inventory which services actually exist before promising a menu, inventory, or battle. Implement only the requested slice and define any new state contract explicitly.
