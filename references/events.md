# Map events and common events

## Map-event rules

Sources: [event creation](https://silversecond.com/WolfRPGEditor/Help/04eventmain.html), [event window](https://silversecond.com/WolfRPGEditor/Help/04eventwindowB.html).

Choose the event layer, then create/edit at a map position. Each page has appearance, movement, trigger, conditions, and commands. When several page conditions match, the highest-numbered page wins; a later unconditional page can hide earlier ones. Distinguish a page's eligibility from how the player activates it.

Confirm-key events need a reachable interaction position. Player-touch and event-touch triggers differ. Autorun blocks ordinary event progression; parallel execution can continue alongside other events and repeats while eligible. A one-time autorun needs a completion state that makes its page ineligible. Do not rely on a blocking command to make an otherwise unbounded loop safe.

For a non-starting event, inspect the winning page, activation condition, trigger, collision/through setting, actual player position, and any existing autorun before rewriting commands. Movement route completion can block when the target cannot reach its destination; test obstruction.

## Reusable event design

Sources: [common-event settings](https://silversecond.com/WolfRPGEditor/Help/02commonev.html), [calling events](https://silversecond.com/WolfRPGEditor/Help/04ev_common.html).

Common events are callable from across the game. Modes include call-only, autorun, conditional parallel, and always-parallel. Call-only numeric inputs 1–4 populate CSelf0–3; string inputs 1–4 populate CSelf5–8. A configured CSelf result can be returned to a caller-selected variable. Treat this as the event's interface and preserve the caller's contract.

Conditional parallel common events can stop mid-flow when their condition becomes false; map transfers interrupt and may restart them. Initialize scratch values on entry and plan cleanup of pictures, input locks, and temporary effects. Do not assume interrupted cleanup commands run.

Calls can target installed common events or events on the current map. By-name common calls choose the higher-numbered event if names collide; invalid names do nothing. Prefer a verified unique name or a stable ID according to project conventions. Reserve/queue behavior starts after the current event finishes and differs from immediate insertion.

## Recipes as designs, not import syntax

### Persistent reward chest

Source: [official chest tutorial](https://silversecond.com/WolfRPGEditor/Guide/EV_006.html), author ミケ.

Use two pages and an unused map-event Self variable. The closed page gives the reward through the project's existing item-change common event, then records completion. The higher opened page is eligible when completion is set; it changes the graphic and cannot grant another reward. Find the real item-change event and inputs in this project rather than assuming the tutorial's sample numbers.

Test initial inventory, first activation, repeat activation, leaving/returning, and save/load. Also test inventory-full or other rejected-reward behavior if the project has it; decide whether completion is recorded only after success. Copying a chest onto the map creates another event identity, so verify that its state is independent.

### Door or transfer

Record source map/event/page, destination registered map ID, coordinates, facing, fade sequence, and activation trigger. Place arrival outside the return trigger or add an appropriate re-entry guard. Test both directions and rapid re-entry; ensure control returns after fades and route waits.

### One-time cutscene

Use an explicit state progression: eligible, running, complete. Define when the complete state becomes durable and what saving/loading during the scene should do. Restore player control and presentation on every supported exit. Use the project's existing cutscene conventions rather than introducing a second global lock.

### Background service

Poll with a deliberate wait appropriate to the required responsiveness. Separate a key's current held state from a one-press action; suppress repeated activation as needed. Test while another event shows dialogue and across map transitions. Multiple parallel events writing one variable or picture ID need an ownership rule.

## Event handoff format

When native edits are unavailable, provide map/common-event identity, page order and eligibility, trigger, graphic/movement settings, variable allocations, ordered command flow, call signatures, and test steps. Label it an editor recipe. Only label code importable after its actual syntax has passed matching-editor readback.
