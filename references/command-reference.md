# Event command reference

This is an operational reference, not an opcode schema. Names vary by translation. Generate each unfamiliar command in the matching editor before changing its serialized parameters. Links identify the official command pages reviewed on 2026-10-20; a current-manual feature still needs a version check in an older binary.

## Message / Show Message / 文章の表示

[Source](https://silversecond.com/WolfRPGEditor/Help/04ev_text.html).

Normal messages, comments, and debug output are separate command modes. Comments do not show to players. A leading `@N` line sets the portrait number in Sys0 before the message; displaying the portrait still requires the game's common-event presentation system. A blank project does not acquire a message window or portraits merely from this setting. A parallel event can forcibly interrupt displayed text. Keep interruption coordinated with input and picture cleanup.

For dialogue work, inspect the message common events and existing portrait conventions first. Preserve authored wording and control codes. Test pagination, names, and font coverage with the actual window dimensions.

## Choices / 選択肢

[Source](https://silversecond.com/WolfRPGEditor/Help/04ev_select.html).

Up to ten choices can have separate branches. Configure cancellation explicitly, including disabled cancel or a dedicated branch. Empty options disappear, including options whose variable substitutions become empty. If every option is empty, the command is skipped. Formatting can carry from one option into later options; reset formatting where needed. A choice immediately following a message can remain visible with that message. Optional left/right and forced-interrupt branches support richer menus; forced interruption comes from another parallel event.

## Set Variable / 変数操作

[Source](https://silversecond.com/WolfRPGEditor/Help/04ev_value.html).

Choose destination, arithmetic operation, operands, and literal/reference interpretation separately. Indirect destination uses a variable containing an encoded variable address; this is different from assigning the address itself. The no-reference option allows a large number to remain a literal. The real-number intermediate option retains fractional intermediate arithmetic before the stored integer is truncated. For example, a multiplier computed as 3/2 differs with integer versus real intermediates. The ±999999 clamp avoids crossing into the reference range when numbers are later used in reference-aware fields.

For multi-variable operations, confirm the emitted count/range with a small example; do not infer inclusive endpoints from translated labels.

## Set Variable+ / 変数操作＋

[Source](https://silversecond.com/WolfRPGEditor/Help/04ev_valuenext.html).

Use this family to retrieve engine state rather than reconstruct it from guessed memory: character/map positions and dimensions, picture state, string information, and related runtime properties. Select the exact property in the installed editor and inspect its units. Map coordinates, precise half-tile coordinates, screen pixels, and effect-adjusted positions are not interchangeable. Use named variables to record the coordinate space and scale of calculated values.

Before a distance, hit-test, or HUD calculation, read one known object at a known position and compare the returned values. Avoid baking a coordinate conversion into multiple event copies.

## Set String / 文字列操作

[Source](https://silversecond.com/WolfRPGEditor/Help/04ev_string.html).

String operations include assignment, append, destructive line/character extraction, literal or regex replacement/extraction, file I/O, keyboard entry, and hidden-code execution. Some extraction modes consume the source; distinguish copying from cutting. File reads can return `<NoFile>`; substring operations may return `<<NotFound>>` rather than an empty result. Directory listing does not enumerate encrypted folder contents. Preserve newline-delimited results until the consumer has intentionally parsed them.

Regex behavior is engine-specific. Variable substitution inside regex uses `<<...>>` around the substitution; do not paste a host-language regex without testing it. Path restrictions and encoding differ from ordinary desktop Python operations. See [advanced operations](advanced-operations.md).

## Numeric / string conditions

Sources: [numeric](https://silversecond.com/WolfRPGEditor/Help/04ev_ifvalue.html), [string](https://silversecond.com/WolfRPGEditor/Help/04ev_ifstring.html).

Branches are evaluated top-down; the first matching branch wins. Put a narrower condition before a broader overlapping one. Add an otherwise branch where needed. Numeric comparisons include strict/inclusive inequalities, equality, inequality, and bit-mask containment. Bit containment means `(value & mask) == mask`; mask zero always matches.

String operations include equality, inequality, containment, prefix, suffix, and regex matching in documented releases. Case, whitespace, newlines, and substitution affect results. Do not use a language's generic truthiness in place of the actual event comparison.

## DB operations / DB操作

[Source](https://silversecond.com/WolfRPGEditor/Help/04ev_db.html).

Ordinary runtime assignment writes Variable DB or XY arrays; ordinary reads can target all three DB kinds. DB operations can also retrieve names/counts, initialize data, copy/sort/insert/remove records, and exchange CSV. Record insertion/removal shifts later IDs. Initializing uses type-defined defaults, which can differ from the editor's game-start values.

Named and numbered XY arrays are separate namespaces: numeric text in name mode does not refer to the numbered array. For Variable DB entries whose names come from their first string field, name resolution changed in 3.566 to follow runtime-renamed data; older compatibility behavior differs. Prefer stable IDs for mutable character names. CSV-based User DB replacement also needs scrutiny of cached names.

## Key Input / キー入力

[Source](https://silversecond.com/WolfRPGEditor/Help/04ev_keyinput.html).

Modes distinguish held state, wait-until-pressed, newly pressed, released, and held-frame duration. No matching basic input returns zero. Direction codes follow a numeric keypad: 2 down, 4 left, 6 right, 8 up, with diagonals 1/3/7/9. Keyboard/pad codes use a different number space. Mouse input includes button state, position, and wheel delta. Analog axes use scaled integers; touch tracking IDs are identities rather than stable touch-list positions.

Synthetic input applies next frame. Keyboard synthesis can bypass a device-key prohibition, while prohibited basic input also blocks synthetic basic actions. Distinguish disabling movement from disabling event input. Restore changed permissions on exit.

## Pictures / ピクチャ

[Source](https://silversecond.com/WolfRPGEditor/Help/04ev_picture.html).

One picture ID owns one displayed picture. IDs control layering; reuse can overwrite unrelated UI. Display/move/erase and delayed-action reset are different operations. Specify origin, pixel coordinates, opacity (0–255), scale, blend, duration, and activation delay deliberately. Rotation is in tenths of a degree. Delayed actions are not saved. A scroll-linked picture follows map scrolling; map zoom needs corresponding picture treatment.

Direct files, string-selected files, text pictures, and generated windows have different parameters. Sheet pattern numbers start at one. For smooth slow movement, keep higher-precision state in variables instead of repeatedly restarting a subpixel movement that rounds away. See [advanced operations](advanced-operations.md) for layer bands and effects.

## Effect / エフェクト

[Source](https://silversecond.com/WolfRPGEditor/Help/04ev_effect.html).

Effects target pictures, characters, or the map and include tint, flashes, offsets, scale/rotation correction, shaking, animation, masks, and layer operations. Picture effects are independent of the base Picture command state; resetting one layer of state may leave the other active. Effect-adjusted rendering is not reflected in coordinates returned by Set Variable+. Transformation effects do not support every picture type, especially text, generated shapes, and video.

Assign one owner for each continuously updated transform. When debugging misalignment, inspect base coordinates, effect offsets, map zoom, scroll link, origin, and window scaling independently. Clean up the specific effect rather than resetting the game's entire presentation state.

## Sound / サウンド

[Source](https://silversecond.com/WolfRPGEditor/Help/04ev_sound.html).

Sound commands distinguish BGM, BGS, and SE; database selection, variable selection, and direct filename routes differ. Fade durations use frames; seek offsets generally use milliseconds except MIDI ticks. Pan uses -255 left through 0 center to 255 right. Channels allow independent BGS/SE control; -1 on a channel-stop operation stops all channels. Repeated same-channel SE can cut off the previous sound.

Direct filename replay of a currently playing BGM/BGS can update parameters without restarting. Preserve a game's channel allocation so a voice stop does not kill effects. Read loop metadata/explicit offsets consistently and verify by listening; container extension alone does not prove a seamless loop.

## Save / Load / セーブ・ロード操作

[Source](https://silversecond.com/WolfRPGEditor/Help/04ev_file.html).

Save/load works with full game state or partial variable/string exchange. Successful load ends the current event and restores saved state, but does not resume the event's command pointer. Loading from a parallel event is unsupported. Partial writes to a nonexistent save do not create full Variable DB state; perform a full save first when a normal loadable game slot is required.

Missing-save reads return zero/empty values, so do not mistake these for proof a save exists. Saved Sys24 can be read to distinguish existence. File writes may be committed at frame end; avoid scattering repeated writes across frames or concurrently touching several huge slots. Cutscene recovery must be state-based rather than depend on continuing after the save command.

## Party Sprite / パーティ画像

[Source](https://silversecond.com/WolfRPGEditor/Help/04ev_party.html).

This family controls walking sprites/followers, not necessarily the RPG character roster. It can insert, delete, replace, hide, remember/restore sprites, gather followers, and control following/synchronization. The engine supports a leader and up to five followers in this system. Following normally uses the leader's movement speed; independent follower routes/speeds require the appropriate following mode. Mixing half-step/full-step settings can break the recorded follow path.

Use Basic System party-management events for game roster changes; use sprite control for presentation where appropriate. Restore follower behavior after a cutscene.

## Tile operations / チップ処理

[Source](https://silversecond.com/WolfRPGEditor/Help/04ev_chip.html).

Runtime tile operations change tile properties, switch a tileset, or overwrite a rectangular map region. These changes reset on map transfer. Changing a tile's property set replaces the configured properties; clearing checkboxes is not a no-op. Record the intended layer, starting X/Y, dimensions, tile ID, and traversal attributes. Persistent world edits need their own durable state and reapplication on map entry; runtime overwrite is not an editor save.

## Transfer / 場所移動

[Source](https://silversecond.com/WolfRPGEditor/Help/04ev_movepos.html).

Target values include event IDs ≥0, -1 for this event/calling map event, -2 for leader, and -3 through -7 for followers. Select destination map/coordinates, direction, and transition explicitly. The destination picker shows saved map data, so save map edits before relying on it. Changing a character's map/position is separate from animating a move route.

## Event control / イベント制御

[Source](https://silversecond.com/WolfRPGEditor/Help/04ev_control.html).

Commands cover loops/break/continue, counted loops, labels, waits, move-route completion, transitions, event termination, temporary erasure, reset, and exit. Temporary erasure lasts until leaving the map; it is not a durable completion flag. Transition preparation freezes drawing while logic continues; execution resumes drawing. A wait uses game frames, not a universal millisecond duration. Match it to the configured FPS.

Avoid jumping into/out of nested loop bodies without verifying loop-counter effects. Ensure every prepared transition has a reachable execute path and every suspended input/movement state has an exit path.

## Move Route / 動作指定

[Source](https://silversecond.com/WolfRPGEditor/Help/04ev_movesettingB.html).

Move routes combine movement, turning, animation/graphic changes, movement parameters, and options. Verify the target and whether execution repeats or waits for completion. An unreachable movement plus completion wait can stall a scene. Before replacing a route, inspect whether another autorun or parallel event reissues it each frame. Readback of one route is insufficient when another event immediately overwrites it.

## Common-event call / コモンイベント

See [events](events.md) and [state/database](state-and-databases.md). The installed event and its defined arguments are the API. A name, ID, deferred call, and map-page insertion are different choices. Do not copy a sample call's opaque argument flags without generating the corresponding command in the target editor.

## Download / ダウンロード

[Source](https://silversecond.com/WolfRPGEditor/Help/04ev_download.html).

The advanced-command option exposes this family. It can retrieve files, send requests, and populate a string. Initialize the destination/status before starting: a failed request can leave its old string intact. Sys48 documents -1 failure, 0 active, 1 complete. Choose wait or background operation deliberately. The engine throttles repeated connections; do not defeat it with a tight retry loop. Build offline fallback and bounded retries for a requested network feature.

## Pro commands

[Source](https://silversecond.com/WolfRPGEditor/Help/04ev_pro_command.html).

Pro-only commands include restart, main-event interruption, per-file encryption-key operations, and screenshot/picture export. Confirm edition/capability instead of assuming a translated menu indicates entitlement. Interrupting a main event can stop its wait without cancelling the underlying route/download/effect. Write separate cleanup for such operations. Do not introduce a Pro-only dependency into a Free project as an incidental implementation choice.
