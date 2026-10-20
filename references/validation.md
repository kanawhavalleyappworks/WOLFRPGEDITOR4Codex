# Debugging, playtesting, and distribution

## Engine evidence

Sources: [debug commands](https://silversecond.com/WolfRPGEditor/Help/01debug.html), [basic controls](https://silversecond.com/WolfRPGEditor/Help/01control.html).

Start test play from the editor (`Ctrl+T`; F9 also works in relevant editor windows). F9 means something different inside a running test: variable inspection. Test-play tools documented in the current manual include F3 debug window, F7 picture list, F8 debug data, and F9 variable list. These are not available in an ordinary player launch. Inspect the installed release before relying on a shortcut.

Capture the affected map/event/common-event identity and line when an error appears. F3 output can be saved as `Log.txt` beside `Game.exe`. Use minimal temporary diagnostics and remove them afterward.

Variable watch instrumentation can disable common-event optimization and change timing and overflow behavior. A bug disappearing while watched is not proof it is fixed; retest without instrumentation. Hot reload is useful for iteration, but a clean launch remains necessary evidence.

## Diagnose by symptom

| Symptom | First investigation |
| --- | --- |
| Only a later event page runs | Inspect page order and every eligible condition |
| Event does not activate | Winning page, trigger, reach/collision, active autorun |
| Game locks or command-count error | Repeating autorun/parallel flow, loop termination, missing waits, recursive calls |
| Reward repeats | Persistent flag, owning event identity, completion page condition |
| Variable DB change seems absent | New game versus loaded save, stored schema and initialization |
| Sprite appears split | Animation/direction settings, dimensions, filename suffix |
| Asset missing only in distribution | Registered path, copied files, package settings and required fonts/audio |
| Text becomes garbled | Source encoding, old-file import language, font glyph coverage |

These are investigation paths, not automatic repairs. Produce a small reproduction before changing shared engine/system settings.

## Verify the requested behavior

Use a fresh game to test initialization. If persistence matters, leave/re-enter the map and save/reload after changing state. If supporting existing saves, load a representative pre-change save too. Confirm both positive and negative branches: cancellation, insufficient items/money, already-complete events, blocked routes, and interrupted background logic as relevant.

Record what actually ran. Hash comparison only detects changed bytes; text parsing only checks a file representation; editor readback only establishes what was imported. None alone proves player input, graphics, sound, timing, or save compatibility.

## Build and distribution

Source: [game-data creation](https://silversecond.com/WolfRPGEditor/Help/02gamemake.html).

Use the editor's game-data creation flow into a separate output directory. Preserve the editable source and keep work files, baselines, and backups out of the distribution. The documented export modes can copy data unencrypted, encrypt all Data, or encrypt selected folders. For partial updates, encryption-version consistency matters; mixed encryption versions can fail to load. Follow the project's established settings and inspect the generated package.

Launch the exported game independently. Check title/new game, the changed feature, assets/audio, save/load, and return paths. An editor playtest does not verify packaging. Do not include editor-only exchange text under the assumption the runtime needs it.

This package includes no editor executable, binary parser, GUI automation provider, engine-backed test harness, or proof of a particular project's compatibility. If WOLF or desktop control is unavailable, deliver the completed static work and state exactly which engine checks remain.
