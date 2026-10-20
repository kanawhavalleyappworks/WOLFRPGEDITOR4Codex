# Database type/field locator: sample 3.691

English labels from the inspected 3.691 translation package: translation by Yumu, edited by Anya and Lolo; sample-data translation by Yumu. Original engine/Basic System by SmokingWOLF. See [sources and credits](sources.md). Reviewed 2026-10-20. This is an installation snapshot, not an engine-version-independent ID registry.

These are observed schema labels, not full sample data or a serializer. Storage codes are copied as opaque observed values. Names may be abbreviated in the source. Inspect the target project before applying an address. No item records, character stats, graphics, audio, or full event bodies are bundled.

## User DB type 0: Skills

| Field | Label | Observed storage code |
| --- | --- | --- |
| 0 | Skill Name | 2000 |
| 1 | Description | 2001 |
| 2 | ┏ Effect Target    | 1000 |
| 3 | (If Used) ┗ Event Number | 1001 |
| 4 | ┏ What to Consume? | 1002 |
| 5 | ┗ Points Consumed   | 1003 |
| 6 | Usable When? | 1004 |
| 7 | SuccessRate\[%\] \[-1:Accuracy\] | 1005 |
| 8 | ┏ What's Affected?                  | 1006 |
| 9 | ┣ Base Amount \[Fixed Value\] | 1007 |
| 10 | ┣ Attack Influence \[%\]            | 1008 |
| 11 | ┣ Magic Influence \[%\]            | 1009 |
| 12 | ┗ Variance \[±%\]                      | 1010 |
| 13 | Use Message \[Map\] (Name... | 2002 |
| 14 | Use Message \[Battle\] (Name... | 2003 |
| 15 | Failure Message (Target... | 2004 |
| 16 | Priority Option | 1011 |
| 17 | Element | 1012 |
| 18 | Repeat Times/Weapon Effect | 1013 |
| 19 | Animation | 1014 |
| 20 | Item Required? \[Consume\] | 1015 |
| 21 | When Skills Are Limited... | 1016 |
| 22 | Add State 1              | 1017 |
| 23 | ┗ State 1 Rate \[%\] | 1018 |
| 24 | Add State 2              | 1019 |
| 25 | ┗ State 2 Rate \[%\] | 1020 |
| 26 | Add State 3              | 1021 |
| 27 | ┗ State 3 Rate \[%\] | 1022 |
| 28 | Remove State 1 | 1023 |
| 29 | Remove State 2 | 1024 |
| 30 | Remove State 3 | 1025 |
| 31 | Weapon-Based Accuracy ±% | 1026 |
| 32 | Critical Rate \[%\] (-1:None) | 1027 |
| 33 | Target's Evasion | 1028 |
| 34 | Target's Def/Magic Def | 1029 |
| 35 | Return Effects to Self? | 1030 |
| 36 | Timing to Execute Skill | 1031 |

## User DB type 1: ┗ Animations

| Field | Label | Observed storage code |
| --- | --- | --- |
| 0 | Image File | 2000 |
| 1 | Image Horizontal Divisions | 1000 |
| 2 | Image Vertical Divisions | 1001 |
| 3 | Total Animation Patterns | 1002 |
| 4 | 1 Pattern Wait \[Frames\] | 1003 |
| 5 | Blend Mode | 1004 |
| 6 | Zoom | 1005 |
| 7 | Display Option | 1006 |
| 8 | Damage Display Wait \[Frames | 1007 |
| 9 | Sound Effect | 2001 |
| 10 | Sound Effect Delay \[Frames\] | 1008 |
| 11 | \[Color\] R Adjust (±100) | 1009 |
| 12 | \[Color\] G Adjust (±100) | 1010 |
| 13 | \[Color\] B Adjust (±100) | 1011 |
| 14 | Process By \[Ignore Settings\] | 1012 |

## User DB type 2: Items

| Field | Label | Observed storage code |
| --- | --- | --- |
| 0 | Item Name | 2000 |
| 1 | Description \[Up to 2 Lines\] | 2001 |
| 2 | Usable When? | 1000 |
| 3 | ■Effect Type                        | 1001 |
| 4 | ┣ \[2\]: Skill to Use                 | 1002 |
| 5 | ┃┗ Battle Message on Use | 1003 |
| 6 | ┗ \[3\]: Event to Call              | 1004 |
| 7 | Usage Limit                                | 1005 |
| 8 | ┗ Changes When Consumed? | 1006 |
| 9 | Effect Target | 1007 |
| 10 | HP Recovery \[X% of Max\] | 1008 |
| 11 | ┗ + HP Recovery \[Points\] | 1009 |
| 12 | SP Recovery \[X% of Max\] | 1010 |
| 13 | ┗ + SP Recovery \[Points\] | 1011 |
| 14 | Remove State 1 | 1012 |
| 15 | Remove State 2 | 1013 |
| 16 | Remove State 3 | 1014 |
| 17 | Use Message \[Map\] | 2002 |
| 18 | Use Message \[Battle\] (Name... | 2003 |
| 19 | Sell Price \[0=Can't Sell\] | 1015 |
| 20 | Sound Effect on Use | 2004 |

## User DB type 3: Weapons

| Field | Label | Observed storage code |
| --- | --- | --- |
| 0 | Weapon Name | 2000 |
| 1 | Description \[Up to 2 Lines\] | 2001 |
| 2 | Equipment Type | 1000 |
| 3 | Equippable Slots 1-4 | 1001 |
| 4 | Equippable Slots 5-8 | 1002 |
| 5 | Attack Animation | 1003 |
| 6 | Max HP Change | 1004 |
| 7 | Max SP Change | 1005 |
| 8 | Attack Change | 1006 |
| 9 | Defense Change | 1007 |
| 10 | Magic Attack Change | 1008 |
| 11 | Magic Defense Change | 1009 |
| 12 | Agility Change | 1010 |
| 13 | Accuracy \[%\] Change | 1011 |
| 14 | Evasion \[%\] Change | 1012 |
| 15 | Critical Rate \[%\] Change | 1013 |
| 16 | Equipped, Can't Remove? | 1014 |
| 17 | Sell Price \[0=Can't Sell\] | 1015 |
| 18 | ┏ Add State        | 1016 |
| 19 | ┗ State Rate \[%\] | 1017 |
| 20 | ┏ Change Battle Command | 1018 |
| 21 | ┗ Command to Change       | 1019 |
| 22 | Skill When Used As Item?      | 1020 |
| 23 | ┣ Skill to Use                           | 1021 |
| 24 | ┣ Message \[Map\]                   | 2002 |
| 25 | ┣ Message \[Battle\] (Name... | 2003 |
| 26 | ┗ Item Changes After Use    | 1022 |
| 27 | Exclusive Slots on Equip | 1023 |
| 28 | Element 1 | 1024 |
| 29 | Element 2 | 1025 |

## User DB type 4: Armors

| Field | Label | Observed storage code |
| --- | --- | --- |
| 0 | Armor Name | 2000 |
| 1 | Description \[Up to 2 Lines\] | 2001 |
| 2 | Equipment Type | 1000 |
| 3 | Equippable Slots 1-4 | 1001 |
| 4 | Equippable Slots 5-8 | 1002 |
| 5 | Max HP Change | 1003 |
| 6 | Max SP Change | 1004 |
| 7 | Attack Change | 1005 |
| 8 | Defense Change | 1006 |
| 9 | Magic Attack Change | 1007 |
| 10 | Magic Defense Change | 1008 |
| 11 | Agility Change | 1009 |
| 12 | Accuracy \[%\] Change | 1010 |
| 13 | Evasion \[%\] Change | 1011 |
| 14 | Critical Rate \[%\] Change | 1012 |
| 15 | Equipped, Can't Remove? | 1013 |
| 16 | ┏ Change Battle Command | 1014 |
| 17 | ┗ Command to Change       | 1015 |
| 18 | Sell Price \[0=Can't Sell\] | 1016 |
| 19 | ------------------------------- | 2002 |
| 20 | Skill When Used As Item?      | 1017 |
| 21 | ┣ Skill to Use                           | 1018 |
| 22 | ┣ Message \[Map\]                   | 2003 |
| 23 | ┣ Message \[Battle\] (Name... | 2004 |
| 24 | ┗ Item Changes After Use    | 1019 |
| 25 | Element Resist/Weak A      | 1020 |
| 26 | ┗ Element A Def Rate ±% | 1021 |
| 27 | Element Resist/Weak B      | 1022 |
| 28 | ┗ Element B Def Rate ±% | 1023 |
| 29 | Element Resist/Weak C      | 1024 |
| 30 | ┗ Element C Def Rate ±% | 1025 |
| 31 | Exclusive Slots on Equip | 1026 |
| 32 | State Resist A                 | 1027 |
| 33 | ┗ State A Def Rate ±% | 1028 |
| 34 | State Resist B                 | 1029 |
| 35 | ┗ State B Def Rate ±% | 1030 |
| 36 | State Resist C                 | 1031 |
| 37 | ┗ State C Def Rate ±% | 1032 |

## User DB type 5: ┗ Equipment Types

| Field | Label | Observed storage code |
| --- | --- | --- |
| 0 | Equipment Type Name | 2000 |

## User DB type 6: Battle Commands

| Field | Label | Observed storage code |
| --- | --- | --- |
| 0 | Command Name | 2000 |
| 1 | Description | 2001 |
| 2 | Effect on Selection | 1000 |
| 3 | Condition to Disable | 1001 |

## User DB type 7: Element Names

| Field | Label | Observed storage code |
| --- | --- | --- |
| 0 | Element Name | 2000 |

## User DB type 8: States

| Field | Label | Observed storage code |
| --- | --- | --- |
| 0 | State Name | 2000 |
| 1 | Display Type | 1000 |
| 2 | Display Name | 2001 |
| 3 | Color Change: Allies Only | 1001 |
| 4 | Duration in Turns \[-1:Infinite\] | 1002 |
| 5 | ┗ Duration Variance \[±\] | 1003 |
| 6 | Removal Timing | 1004 |
| 7 | Category (Battle/Map) | 1005 |
| 8 | ┏ Removed by Physical Dmg | 1006 |
| 9 | ┗ Removed by Magic Dmg    | 1007 |
| 10 | When This State Is Stacked... | 1008 |
| 11 | ┗ Make It Into This State | 1009 |
| 12 | Apply Message (Name... | 2002 |
| 13 | Restriction Msg (Blank:None) | 2003 |
| 14 | Remove Message (Name... | 2004 |
| 15 | Count as Fainted? | 1010 |
| 16 | Action Restriction | 1011 |
| 17 | Skill Limitation | 1012 |
| 18 | All Other States... | 1013 |
| 19 | Removed by Full Recovery? | 1014 |
| 20 | Physical Damage Taken Rate | 1015 |
| 21 | Magic Damage Taken Rate | 1016 |
| 22 | HP Change\[±%\](at Turn End) | 1017 |
| 23 | HP Change \[±\] (at Turn End) | 1018 |
| 24 | SP Change\[±%\](at Turn End) | 1019 |
| 25 | SP Change \[±\] (at Turn End) | 1020 |
| 26 | Max HP Change \[%\] | 1021 |
| 27 | Max SP Change \[%\] | 1022 |
| 28 | Attack Change \[%\] | 1023 |
| 29 | Defense Change \[%\] | 1024 |
| 30 | Magic Attack Change \[%\] | 1025 |
| 31 | Magic Defense Change \[%\] | 1026 |
| 32 | Agility Change \[%\] | 1027 |
| 33 | Accuracy (%) Change \[±\] | 1028 |
| 34 | Evasion (%) Change \[±\] | 1029 |
| 35 | Critical Rate (%) Change \[±\] | 1030 |
| 36 | HP Change ±(1 Step on Map) | 1031 |
| 37 | SP Change ± (1 Step on Map) | 1032 |
| 38 | Enemy Targeting Level | 1033 |
| 39 | ------------- | 1034 |
| 40 | Counterattack? (with Skill)      | 1035 |
| 41 | ┣ Trigger on Element Hit         | 1036 |
| 42 | ┣ Counter Trigger Rate \[%\]     | 1037 |
| 43 | ┣ Counter Message (Target... | 2005 |
| 44 | ┗ Stats to Use for Skill             | 1038 |
| 45 | Portrait for State | 2006 |

## User DB type 9: Enemies

| Field | Label | Observed storage code |
| --- | --- | --- |
| 0 | Enemy Name | 2000 |
| 1 | Image File | 2001 |
| 2 | Max HP | 1000 |
| 3 | Max SP | 1001 |
| 4 | Attack | 1002 |
| 5 | Defense | 1003 |
| 6 | Magic Attack | 1004 |
| 7 | Magic Defense | 1005 |
| 8 | Agility | 1006 |
| 9 | Base Accuracy \[%\] | 1007 |
| 10 | Base Evasion \[%\] | 1008 |
| 11 | Critical Rate \[%\] | 1009 |
| 12 | Experience | 1010 |
| 13 | Money | 1011 |
| 14 | Item Drop                        | 1012 |
| 15 | ┗ Drop Rate \[Item\] \[%\] | 1013 |
| 16 | Weapon Drop                         | 1014 |
| 17 | ┗ Drop Rate \[Weapon\] \[%\] | 1015 |
| 18 | Armor Drop                        | 1016 |
| 19 | ┗ Drop Rate \[Armor\] \[%\] | 1017 |
| 20 | Number of Actions | 1018 |
| 21 | ┏ Transform Condition | 1019 |
| 22 | ┃┗  \[A\] Value                   | 1020 |
| 23 | ┣ Transforms Into          | 1021 |
| 24 | ┣ Transform Option      | 1022 |
| 25 | ┗ Call Event \[-1:None\]  | 1023 |

## User DB type 10: ┣ Enemy Action AI

| Field | Label | Observed storage code |
| --- | --- | --- |
| 0 | &lt;Action 1&gt; Condition ▼▼▼   | 1000 |
| 1 | ┣1 Target of Use \[If 1 Target\]   | 1001 |
| 2 | ┣1 Action to Perform               | 1002 |
| 3 | ┗1 When Condition Isn't Met | 1003 |
| 4 | &lt;Action 2&gt; Condition ▼▼▼   | 1004 |
| 5 | ┣2 Target of Use \[If 1 Target\]   | 1005 |
| 6 | ┣2 Action to Perform               | 1006 |
| 7 | ┗2 When Condition Isn't Met | 1007 |
| 8 | &lt;Action 3&gt; Condition ▼▼▼   | 1008 |
| 9 | ┣3 Target of Use \[If 1 Target\]   | 1009 |
| 10 | ┣3 Action to Perform               | 1010 |
| 11 | ┗3 When Condition Isn't Met | 1011 |
| 12 | &lt;Action 4&gt; Condition ▼▼▼   | 1012 |
| 13 | ┣4 Target of Use \[If 1 Target\]   | 1013 |
| 14 | ┣4 Action to Perform               | 1014 |
| 15 | ┗4 When Condition Isn't Met | 1015 |
| 16 | &lt;Action 5&gt; Condition ▼▼▼   | 1016 |
| 17 | ┣5 Target of Use \[If 1 Target\]   | 1017 |
| 18 | ┣5 Action to Perform               | 1018 |
| 19 | ┗5 When Condition Isn't Met | 1019 |
| 20 | &lt;Action 6&gt; Condition ▼▼▼   | 1020 |
| 21 | ┣6 Target of Use \[If 1 Target\]   | 1021 |
| 22 | ┣6 Action to Perform               | 1022 |
| 23 | ┗6 When Condition Isn't Met | 1023 |
| 24 | &lt;Action 7&gt; Condition ▼▼▼   | 1024 |
| 25 | ┣7 Target of Use \[If 1 Target\]   | 1025 |
| 26 | ┣7 Action to Perform               | 1026 |
| 27 | ┗7 When Condition Isn't Met | 1027 |
| 28 | &lt;Action 8&gt; Condition ▼▼▼   | 1028 |
| 29 | ┣8 Target of Use \[If 1 Target\]   | 1029 |
| 30 | ┣8 Action to Perform               | 1030 |
| 31 | ┗8 When Condition Isn't Met | 1031 |
| 32 | &lt;Action 9&gt; Condition ▼▼▼   | 1032 |
| 33 | ┣9 Target of Use \[If 1 Target\]   | 1033 |
| 34 | ┣9 Action to Perform               | 1034 |
| 35 | ┗9 When Condition Isn't Met | 1035 |
| 36 | &lt;Action 10&gt; Condition ▼▼▼ | 1036 |
| 37 | ┣10 Target of Use \[If 1 Target\]  | 1037 |
| 38 | ┣10 Action to Perform              | 1038 |
| 39 | ┗10 When Condition Isn't Met | 1039 |
| 40 | &lt;Action 11&gt; Condition ▼▼▼ | 1040 |
| 41 | ┣11 Target of Use \[If 1 Target\]  | 1041 |
| 42 | ┣11 Action to Perform              | 1042 |
| 43 | ┗11 When Condition Isn't Met | 1043 |
| 44 | &lt;Action 12&gt; Condition ▼▼▼ | 1044 |
| 45 | ┣12 Target of Use \[If 1 Target\]  | 1045 |
| 46 | ┣12 Action to Perform              | 1046 |
| 47 | ┗12 When Condition Isn't Met | 1047 |

## User DB type 11: ┣ Element Resistances

| Field | Label | Observed storage code |
| --- | --- | --- |
| 0 | &lt;\\udb\[7:\\d\[0\]\]&gt;Effect\[%\] | 1000 |
| 1 | &lt;\\udb\[7:\\d\[0\]\]&gt;Effect\[%\] | 1001 |
| 2 | &lt;\\udb\[7:\\d\[0\]\]&gt;Effect\[%\] | 1002 |
| 3 | &lt;\\udb\[7:\\d\[0\]\]&gt;Effect\[%\] | 1003 |
| 4 | &lt;\\udb\[7:\\d\[0\]\]&gt;Effect\[%\] | 1004 |
| 5 | &lt;\\udb\[7:\\d\[0\]\]&gt;Effect\[%\] | 1005 |
| 6 | &lt;\\udb\[7:\\d\[0\]\]&gt;Effect\[%\] | 1006 |
| 7 | &lt;\\udb\[7:\\d\[0\]\]&gt;Effect\[%\] | 1007 |
| 8 | &lt;\\udb\[7:\\d\[0\]\]&gt;Effect\[%\] | 1008 |
| 9 | &lt;\\udb\[7:\\d\[0\]\]&gt;Effect\[%\] | 1009 |
| 10 | &lt;\\udb\[7:\\d\[0\]\]&gt;Effect\[%\] | 1010 |
| 11 | &lt;\\udb\[7:\\d\[0\]\]&gt;Effect\[%\] | 1011 |
| 12 | &lt;\\udb\[7:\\d\[0\]\]&gt;Effect\[%\] | 1012 |
| 13 | &lt;\\udb\[7:\\d\[0\]\]&gt;Effect\[%\] | 1013 |
| 14 | &lt;\\udb\[7:\\d\[0\]\]&gt;Effect\[%\] | 1014 |
| 15 | &lt;\\udb\[7:\\d\[0\]\]&gt;Effect\[%\] | 1015 |
| 16 | &lt;\\udb\[7:\\d\[0\]\]&gt;Effect\[%\] | 1016 |
| 17 | &lt;\\udb\[7:\\d\[0\]\]&gt;Effect\[%\] | 1017 |
| 18 | &lt;\\udb\[7:\\d\[0\]\]&gt;Effect\[%\] | 1018 |
| 19 | &lt;\\udb\[7:\\d\[0\]\]&gt;Effect\[%\] | 1019 |
| 20 | &lt;\\udb\[7:\\d\[0\]\]&gt;Effect\[%\] | 1020 |
| 21 | &lt;\\udb\[7:\\d\[0\]\]&gt;Effect\[%\] | 1021 |
| 22 | &lt;\\udb\[7:\\d\[0\]\]&gt;Effect\[%\] | 1022 |
| 23 | &lt;\\udb\[7:\\d\[0\]\]&gt;Effect\[%\] | 1023 |
| 24 | &lt;\\udb\[7:\\d\[0\]\]&gt;Effect\[%\] | 1024 |
| 25 | &lt;\\udb\[7:\\d\[0\]\]&gt;Effect\[%\] | 1025 |
| 26 | &lt;\\udb\[7:\\d\[0\]\]&gt;Effect\[%\] | 1026 |
| 27 | &lt;\\udb\[7:\\d\[0\]\]&gt;Effect\[%\] | 1027 |
| 28 | &lt;\\udb\[7:\\d\[0\]\]&gt;Effect\[%\] | 1028 |
| 29 | &lt;\\udb\[7:\\d\[0\]\]&gt;Effect\[%\] | 1029 |
| 30 | &lt;\\udb\[7:\\d\[0\]\]&gt;Effect\[%\] | 1030 |
| 31 | &lt;\\udb\[7:\\d\[0\]\]&gt;Effect\[%\] | 1031 |
| 32 | &lt;\\udb\[7:\\d\[0\]\]&gt;Effect\[%\] | 1032 |
| 33 | &lt;\\udb\[7:\\d\[0\]\]&gt;Effect\[%\] | 1033 |
| 34 | &lt;\\udb\[7:\\d\[0\]\]&gt;Effect\[%\] | 1034 |
| 35 | &lt;\\udb\[7:\\d\[0\]\]&gt;Effect\[%\] | 1035 |
| 36 | &lt;\\udb\[7:\\d\[0\]\]&gt;Effect\[%\] | 1036 |
| 37 | &lt;\\udb\[7:\\d\[0\]\]&gt;Effect\[%\] | 1037 |
| 38 | &lt;\\udb\[7:\\d\[0\]\]&gt;Effect\[%\] | 1038 |
| 39 | &lt;\\udb\[7:\\d\[0\]\]&gt;Effect\[%\] | 1039 |
| 40 | &lt;\\udb\[7:\\d\[0\]\]&gt;Effect\[%\] | 1040 |
| 41 | &lt;\\udb\[7:\\d\[0\]\]&gt;Effect\[%\] | 1041 |
| 42 | &lt;\\udb\[7:\\d\[0\]\]&gt;Effect\[%\] | 1042 |
| 43 | &lt;\\udb\[7:\\d\[0\]\]&gt;Effect\[%\] | 1043 |
| 44 | &lt;\\udb\[7:\\d\[0\]\]&gt;Effect\[%\] | 1044 |
| 45 | &lt;\\udb\[7:\\d\[0\]\]&gt;Effect\[%\] | 1045 |
| 46 | &lt;\\udb\[7:\\d\[0\]\]&gt;Effect\[%\] | 1046 |
| 47 | &lt;\\udb\[7:\\d\[0\]\]&gt;Effect\[%\] | 1047 |
| 48 | &lt;\\udb\[7:\\d\[0\]\]&gt;Effect\[%\] | 1048 |
| 49 | &lt;\\udb\[7:\\d\[0\]\]&gt;Effect\[%\] | 1049 |
| 50 | &lt;\\udb\[7:\\d\[0\]\]&gt;Effect\[%\] | 1050 |
| 51 | &lt;\\udb\[7:\\d\[0\]\]&gt;Effect\[%\] | 1051 |
| 52 | &lt;\\udb\[7:\\d\[0\]\]&gt;Effect\[%\] | 1052 |
| 53 | &lt;\\udb\[7:\\d\[0\]\]&gt;Effect\[%\] | 1053 |
| 54 | &lt;\\udb\[7:\\d\[0\]\]&gt;Effect\[%\] | 1054 |
| 55 | &lt;\\udb\[7:\\d\[0\]\]&gt;Effect\[%\] | 1055 |
| 56 | &lt;\\udb\[7:\\d\[0\]\]&gt;Effect\[%\] | 1056 |
| 57 | &lt;\\udb\[7:\\d\[0\]\]&gt;Effect\[%\] | 1057 |
| 58 | &lt;\\udb\[7:\\d\[0\]\]&gt;Effect\[%\] | 1058 |
| 59 | &lt;\\udb\[7:\\d\[0\]\]&gt;Effect\[%\] | 1059 |
| 60 | &lt;\\udb\[7:\\d\[0\]\]&gt;Effect\[%\] | 1060 |
| 61 | &lt;\\udb\[7:\\d\[0\]\]&gt;Effect\[%\] | 1061 |
| 62 | &lt;\\udb\[7:\\d\[0\]\]&gt;Effect\[%\] | 1062 |
| 63 | &lt;\\udb\[7:\\d\[0\]\]&gt;Effect\[%\] | 1063 |
| 64 | &lt;\\udb\[7:\\d\[0\]\]&gt;Effect\[%\] | 1064 |
| 65 | &lt;\\udb\[7:\\d\[0\]\]&gt;Effect\[%\] | 1065 |
| 66 | &lt;\\udb\[7:\\d\[0\]\]&gt;Effect\[%\] | 1066 |
| 67 | &lt;\\udb\[7:\\d\[0\]\]&gt;Effect\[%\] | 1067 |
| 68 | &lt;\\udb\[7:\\d\[0\]\]&gt;Effect\[%\] | 1068 |
| 69 | &lt;\\udb\[7:\\d\[0\]\]&gt;Effect\[%\] | 1069 |
| 70 | &lt;\\udb\[7:\\d\[0\]\]&gt;Effect\[%\] | 1070 |
| 71 | &lt;\\udb\[7:\\d\[0\]\]&gt;Effect\[%\] | 1071 |
| 72 | &lt;\\udb\[7:\\d\[0\]\]&gt;Effect\[%\] | 1072 |
| 73 | &lt;\\udb\[7:\\d\[0\]\]&gt;Effect\[%\] | 1073 |
| 74 | &lt;\\udb\[7:\\d\[0\]\]&gt;Effect\[%\] | 1074 |
| 75 | &lt;\\udb\[7:\\d\[0\]\]&gt;Effect\[%\] | 1075 |
| 76 | &lt;\\udb\[7:\\d\[0\]\]&gt;Effect\[%\] | 1076 |
| 77 | &lt;\\udb\[7:\\d\[0\]\]&gt;Effect\[%\] | 1077 |
| 78 | &lt;\\udb\[7:\\d\[0\]\]&gt;Effect\[%\] | 1078 |
| 79 | &lt;\\udb\[7:\\d\[0\]\]&gt;Effect\[%\] | 1079 |
| 80 | &lt;\\udb\[7:\\d\[0\]\]&gt;Effect\[%\] | 1080 |
| 81 | &lt;\\udb\[7:\\d\[0\]\]&gt;Effect\[%\] | 1081 |
| 82 | &lt;\\udb\[7:\\d\[0\]\]&gt;Effect\[%\] | 1082 |
| 83 | &lt;\\udb\[7:\\d\[0\]\]&gt;Effect\[%\] | 1083 |
| 84 | &lt;\\udb\[7:\\d\[0\]\]&gt;Effect\[%\] | 1084 |
| 85 | &lt;\\udb\[7:\\d\[0\]\]&gt;Effect\[%\] | 1085 |
| 86 | &lt;\\udb\[7:\\d\[0\]\]&gt;Effect\[%\] | 1086 |
| 87 | &lt;\\udb\[7:\\d\[0\]\]&gt;Effect\[%\] | 1087 |
| 88 | &lt;\\udb\[7:\\d\[0\]\]&gt;Effect\[%\] | 1088 |
| 89 | &lt;\\udb\[7:\\d\[0\]\]&gt;Effect\[%\] | 1089 |
| 90 | &lt;\\udb\[7:\\d\[0\]\]&gt;Effect\[%\] | 1090 |
| 91 | &lt;\\udb\[7:\\d\[0\]\]&gt;Effect\[%\] | 1091 |
| 92 | &lt;\\udb\[7:\\d\[0\]\]&gt;Effect\[%\] | 1092 |
| 93 | &lt;\\udb\[7:\\d\[0\]\]&gt;Effect\[%\] | 1093 |
| 94 | &lt;\\udb\[7:\\d\[0\]\]&gt;Effect\[%\] | 1094 |
| 95 | &lt;\\udb\[7:\\d\[0\]\]&gt;Effect\[%\] | 1095 |
| 96 | &lt;\\udb\[7:\\d\[0\]\]&gt;Effect\[%\] | 1096 |
| 97 | &lt;\\udb\[7:\\d\[0\]\]&gt;Effect\[%\] | 1097 |
| 98 | &lt;\\udb\[7:\\d\[0\]\]&gt;Effect\[%\] | 1098 |
| 99 | &lt;\\udb\[7:\\d\[0\]\]&gt;Effect\[%\] | 1099 |

## User DB type 12: ┗ State Resistances

| Field | Label | Observed storage code |
| --- | --- | --- |
| 0 | &lt;\\udb\[8:\\d\[0\]\]&gt;S. Rate | 1000 |
| 1 | &lt;\\udb\[8:\\d\[0\]\]&gt;S. Rate | 1001 |
| 2 | &lt;\\udb\[8:\\d\[0\]\]&gt;S. Rate | 1002 |
| 3 | &lt;\\udb\[8:\\d\[0\]\]&gt;S. Rate | 1003 |
| 4 | &lt;\\udb\[8:\\d\[0\]\]&gt;S. Rate | 1004 |
| 5 | &lt;\\udb\[8:\\d\[0\]\]&gt;S. Rate | 1005 |
| 6 | &lt;\\udb\[8:\\d\[0\]\]&gt;S. Rate | 1006 |
| 7 | &lt;\\udb\[8:\\d\[0\]\]&gt;S. Rate | 1007 |
| 8 | &lt;\\udb\[8:\\d\[0\]\]&gt;S. Rate | 1008 |
| 9 | &lt;\\udb\[8:\\d\[0\]\]&gt;S. Rate | 1009 |
| 10 | &lt;\\udb\[8:\\d\[0\]\]&gt;S. Rate | 1010 |
| 11 | &lt;\\udb\[8:\\d\[0\]\]&gt;S. Rate | 1011 |
| 12 | &lt;\\udb\[8:\\d\[0\]\]&gt;S. Rate | 1012 |
| 13 | &lt;\\udb\[8:\\d\[0\]\]&gt;S. Rate | 1013 |
| 14 | &lt;\\udb\[8:\\d\[0\]\]&gt;S. Rate | 1014 |
| 15 | &lt;\\udb\[8:\\d\[0\]\]&gt;S. Rate | 1015 |
| 16 | &lt;\\udb\[8:\\d\[0\]\]&gt;S. Rate | 1016 |
| 17 | &lt;\\udb\[8:\\d\[0\]\]&gt;S. Rate | 1017 |
| 18 | &lt;\\udb\[8:\\d\[0\]\]&gt;S. Rate | 1018 |
| 19 | &lt;\\udb\[8:\\d\[0\]\]&gt;S. Rate | 1019 |
| 20 | &lt;\\udb\[8:\\d\[0\]\]&gt;S. Rate | 1020 |
| 21 | &lt;\\udb\[8:\\d\[0\]\]&gt;S. Rate | 1021 |
| 22 | &lt;\\udb\[8:\\d\[0\]\]&gt;S. Rate | 1022 |
| 23 | &lt;\\udb\[8:\\d\[0\]\]&gt;S. Rate | 1023 |
| 24 | &lt;\\udb\[8:\\d\[0\]\]&gt;S. Rate | 1024 |
| 25 | &lt;\\udb\[8:\\d\[0\]\]&gt;S. Rate | 1025 |
| 26 | &lt;\\udb\[8:\\d\[0\]\]&gt;S. Rate | 1026 |
| 27 | &lt;\\udb\[8:\\d\[0\]\]&gt;S. Rate | 1027 |
| 28 | &lt;\\udb\[8:\\d\[0\]\]&gt;S. Rate | 1028 |
| 29 | &lt;\\udb\[8:\\d\[0\]\]&gt;S. Rate | 1029 |
| 30 | &lt;\\udb\[8:\\d\[0\]\]&gt;S. Rate | 1030 |
| 31 | &lt;\\udb\[8:\\d\[0\]\]&gt;S. Rate | 1031 |
| 32 | &lt;\\udb\[8:\\d\[0\]\]&gt;S. Rate | 1032 |
| 33 | &lt;\\udb\[8:\\d\[0\]\]&gt;S. Rate | 1033 |
| 34 | &lt;\\udb\[8:\\d\[0\]\]&gt;S. Rate | 1034 |
| 35 | &lt;\\udb\[8:\\d\[0\]\]&gt;S. Rate | 1035 |
| 36 | &lt;\\udb\[8:\\d\[0\]\]&gt;S. Rate | 1036 |
| 37 | &lt;\\udb\[8:\\d\[0\]\]&gt;S. Rate | 1037 |
| 38 | &lt;\\udb\[8:\\d\[0\]\]&gt;S. Rate | 1038 |
| 39 | &lt;\\udb\[8:\\d\[0\]\]&gt;S. Rate | 1039 |
| 40 | &lt;\\udb\[8:\\d\[0\]\]&gt;S. Rate | 1040 |
| 41 | &lt;\\udb\[8:\\d\[0\]\]&gt;S. Rate | 1041 |
| 42 | &lt;\\udb\[8:\\d\[0\]\]&gt;S. Rate | 1042 |
| 43 | &lt;\\udb\[8:\\d\[0\]\]&gt;S. Rate | 1043 |
| 44 | &lt;\\udb\[8:\\d\[0\]\]&gt;S. Rate | 1044 |
| 45 | &lt;\\udb\[8:\\d\[0\]\]&gt;S. Rate | 1045 |
| 46 | &lt;\\udb\[8:\\d\[0\]\]&gt;S. Rate | 1046 |
| 47 | &lt;\\udb\[8:\\d\[0\]\]&gt;S. Rate | 1047 |
| 48 | &lt;\\udb\[8:\\d\[0\]\]&gt;S. Rate | 1048 |
| 49 | &lt;\\udb\[8:\\d\[0\]\]&gt;S. Rate | 1049 |
| 50 | &lt;\\udb\[8:\\d\[0\]\]&gt;S. Rate | 1050 |
| 51 | &lt;\\udb\[8:\\d\[0\]\]&gt;S. Rate | 1051 |
| 52 | &lt;\\udb\[8:\\d\[0\]\]&gt;S. Rate | 1052 |
| 53 | &lt;\\udb\[8:\\d\[0\]\]&gt;S. Rate | 1053 |
| 54 | &lt;\\udb\[8:\\d\[0\]\]&gt;S. Rate | 1054 |
| 55 | &lt;\\udb\[8:\\d\[0\]\]&gt;S. Rate | 1055 |
| 56 | &lt;\\udb\[8:\\d\[0\]\]&gt;S. Rate | 1056 |
| 57 | &lt;\\udb\[8:\\d\[0\]\]&gt;S. Rate | 1057 |
| 58 | &lt;\\udb\[8:\\d\[0\]\]&gt;S. Rate | 1058 |
| 59 | &lt;\\udb\[8:\\d\[0\]\]&gt;S. Rate | 1059 |
| 60 | &lt;\\udb\[8:\\d\[0\]\]&gt;S. Rate | 1060 |
| 61 | &lt;\\udb\[8:\\d\[0\]\]&gt;S. Rate | 1061 |
| 62 | &lt;\\udb\[8:\\d\[0\]\]&gt;S. Rate | 1062 |
| 63 | &lt;\\udb\[8:\\d\[0\]\]&gt;S. Rate | 1063 |
| 64 | &lt;\\udb\[8:\\d\[0\]\]&gt;S. Rate | 1064 |
| 65 | &lt;\\udb\[8:\\d\[0\]\]&gt;S. Rate | 1065 |
| 66 | &lt;\\udb\[8:\\d\[0\]\]&gt;S. Rate | 1066 |
| 67 | &lt;\\udb\[8:\\d\[0\]\]&gt;S. Rate | 1067 |
| 68 | &lt;\\udb\[8:\\d\[0\]\]&gt;S. Rate | 1068 |
| 69 | &lt;\\udb\[8:\\d\[0\]\]&gt;S. Rate | 1069 |
| 70 | &lt;\\udb\[8:\\d\[0\]\]&gt;S. Rate | 1070 |
| 71 | &lt;\\udb\[8:\\d\[0\]\]&gt;S. Rate | 1071 |
| 72 | &lt;\\udb\[8:\\d\[0\]\]&gt;S. Rate | 1072 |
| 73 | &lt;\\udb\[8:\\d\[0\]\]&gt;S. Rate | 1073 |
| 74 | &lt;\\udb\[8:\\d\[0\]\]&gt;S. Rate | 1074 |
| 75 | &lt;\\udb\[8:\\d\[0\]\]&gt;S. Rate | 1075 |
| 76 | &lt;\\udb\[8:\\d\[0\]\]&gt;S. Rate | 1076 |
| 77 | &lt;\\udb\[8:\\d\[0\]\]&gt;S. Rate | 1077 |
| 78 | &lt;\\udb\[8:\\d\[0\]\]&gt;S. Rate | 1078 |
| 79 | &lt;\\udb\[8:\\d\[0\]\]&gt;S. Rate | 1079 |
| 80 | &lt;\\udb\[8:\\d\[0\]\]&gt;S. Rate | 1080 |
| 81 | &lt;\\udb\[8:\\d\[0\]\]&gt;S. Rate | 1081 |
| 82 | &lt;\\udb\[8:\\d\[0\]\]&gt;S. Rate | 1082 |
| 83 | &lt;\\udb\[8:\\d\[0\]\]&gt;S. Rate | 1083 |
| 84 | &lt;\\udb\[8:\\d\[0\]\]&gt;S. Rate | 1084 |
| 85 | &lt;\\udb\[8:\\d\[0\]\]&gt;S. Rate | 1085 |
| 86 | &lt;\\udb\[8:\\d\[0\]\]&gt;S. Rate | 1086 |
| 87 | &lt;\\udb\[8:\\d\[0\]\]&gt;S. Rate | 1087 |
| 88 | &lt;\\udb\[8:\\d\[0\]\]&gt;S. Rate | 1088 |
| 89 | &lt;\\udb\[8:\\d\[0\]\]&gt;S. Rate | 1089 |
| 90 | &lt;\\udb\[8:\\d\[0\]\]&gt;S. Rate | 1090 |
| 91 | &lt;\\udb\[8:\\d\[0\]\]&gt;S. Rate | 1091 |
| 92 | &lt;\\udb\[8:\\d\[0\]\]&gt;S. Rate | 1092 |
| 93 | &lt;\\udb\[8:\\d\[0\]\]&gt;S. Rate | 1093 |
| 94 | &lt;\\udb\[8:\\d\[0\]\]&gt;S. Rate | 1094 |
| 95 | &lt;\\udb\[8:\\d\[0\]\]&gt;S. Rate | 1095 |
| 96 | &lt;\\udb\[8:\\d\[0\]\]&gt;S. Rate | 1096 |
| 97 | &lt;\\udb\[8:\\d\[0\]\]&gt;S. Rate | 1097 |
| 98 | &lt;\\udb\[8:\\d\[0\]\]&gt;S. Rate | 1098 |
| 99 | &lt;\\udb\[8:\\d\[0\]\]&gt;S. Rate | 1099 |

## User DB type 13: Enemy Groups

| Field | Label | Observed storage code |
| --- | --- | --- |
| 0 | Enemy 1 (◇◇◇◆◇◇◇) | 1000 |
| 1 | Enemy 2 (◇◇◆◇◇◇◇) | 1001 |
| 2 | Enemy 3 (◇◇◇◇◆◇◇) | 1002 |
| 3 | Enemy 4 (◇◆◇◇◇◇◇) | 1003 |
| 4 | Enemy 5 (◇◇◇◇◇◆◇) | 1004 |
| 5 | Enemy 6 (◆◇◇◇◇◇◇) | 1005 |
| 6 | Enemy 7 (◇◇◇◇◇◇◆) | 1006 |
| 7 | ┏ Win Condition | 1007 |
| 8 | ┗ \[A\] Value           | 1008 |
| 9 | ┏ Lose Condition | 1009 |
| 10 | ┗ \[B\] Value            | 1010 |
| 11 | Flee Success Rate \[%\] | 1011 |

## User DB type 14: ------------------------

| Field | Label | Observed storage code |
| --- | --- | --- |

## User DB type 15: Terms

| Field | Label | Observed storage code |
| --- | --- | --- |
| 0 | \[Menu\] Items | 2000 |
| 1 | \[Menu\] Skills | 2001 |
| 2 | \[Menu\] Equip | 2002 |
| 3 | \[Menu\] Save | 2003 |
| 4 | \[Menu\] System | 2004 |
| 5 | \[Stats\] Level | 2005 |
| 6 | \[Stats\] EXP to Next Level | 2006 |
| 7 | \[Stats\] HP Name | 2007 |
| 8 | \[Stats\] SP Name | 2008 |
| 9 | \[Stats\] Attack | 2009 |
| 10 | \[Stats\] Defense | 2010 |
| 11 | \[Stats\] Magic Attack | 2011 |
| 12 | \[Stats\] Magic Defense | 2012 |
| 13 | \[Stats\] Agility | 2013 |
| 14 | \[Stats\] Accuracy | 2014 |
| 15 | \[Stats\] Evasion | 2015 |
| 16 | \[Stats\] Critical Rate | 2016 |
| 17 | \[Stats\] Experience | 2017 |
| 18 | \[Stats\] Currency | 2018 |
| 19 | \[Equip\] Slot 1 &lt;Weapon&gt; | 2019 |
| 20 | \[Equip\] Slot 2 &lt;Armor&gt; | 2020 |
| 21 | \[Equip\] Slot 3 &lt;Armor&gt; | 2021 |
| 22 | \[Equip\] Slot 4 &lt;Armor&gt; | 2022 |
| 23 | \[Equip\] Slot 5 &lt;Armor&gt; | 2023 |
| 24 | \[Equip\] Slot 6 &lt;Armor&gt; | 2024 |
| 25 | \[Equip\] Slot 7 &lt;Armor&gt; | 2025 |
| 26 | \[Equip\] Slot 8 &lt;Armor&gt; | 2026 |
| 27 | \[Save\] Save Message | 2027 |
| 28 | \[Save\] Load Message | 2028 |
| 29 | \[Save\] Save Data Name | 2029 |
| 30 | \[Battle\] Fight Command | 2030 |
| 31 | \[Battle\] Flee Command | 2031 |

## User DB type 16: Images/Sounds

| Field | Label | Observed storage code |
| --- | --- | --- |
| 0 | Window Image File | 2000 |
| 1 | Cursor Image File | 2001 |
| 2 | Message Window Base Image | 2002 |
| 3 | Confirm Sound File | 2003 |
| 4 | Cancel Sound File | 2004 |
| 5 | Cursor Sound File | 2005 |
| 6 | Buzzer Sound File | 2006 |
| 7 | Equip Sound File | 2007 |
| 8 | Unequip Sound File | 2008 |
| 9 | Menu Open Sound File | 2009 |
| 10 | Menu Close Sound File | 2010 |
| 11 | Save Sound File | 2011 |
| 12 | Load Sound File | 2012 |
| 13 | Buy Sound File | 2013 |
| 14 | Sell Sound File | 2014 |
| 15 | Battle Action Sound File | 2015 |
| 16 | Damage Sound File | 2016 |
| 17 | Defeat Sound File | 2017 |
| 18 | Battle Start Sound File | 2018 |
| 19 | Battle Result Sound File | 2019 |
| 20 | Level Up Sound File | 2020 |

## User DB type 17: System Settings

| Field | Label | Observed storage code |
| --- | --- | --- |
| 0 | Maximum Item Quantity | 1000 |
| 1 | Max HP/SP Cap | 1001 |
| 2 | Stats Cap | 1002 |
| 3 | Menu Command 1 | 1003 |
| 4 | Menu Command 2 | 1004 |
| 5 | Menu Command 3 | 1005 |
| 6 | Menu Command 4 | 1006 |
| 7 | Menu Command 5 | 1007 |
| 8 | Menu Command 6 | 1008 |
| 9 | Menu Command 7 | 1009 |
| 10 | Menu Command 8 | 1010 |
| 11 | ■Special Menu A Name    | 2000 |
| 12 | ┗ A: Call Common Event | 1011 |
| 13 | ■Special Menu B Name    | 2001 |
| 14 | ┗ B: Call Common Event | 1012 |
| 15 | ■Special Menu C Name    | 2002 |
| 16 | ┗ C: Call Common Event | 1013 |
| 17 | ■Special Menu D Name    | 2003 |
| 18 | ┗ D: Call Common Event | 1014 |
| 19 | States Display | 1015 |
| 20 | HP/SP After Battle | 1016 |
| 21 | Fainted Members After Battle | 1017 |
| 22 | Equippable Slots | 1018 |
| 23 | When Increasing Stats... | 1019 |
| 24 | Status Portrait Scale | 1020 |
| 25 | Message Portrait Scale | 1021 |
| 26 | \[Battle\] Basic Battle BGM | 2004 |
| 27 | \[Battle\] Display Enemy Gauge | 1022 |
| 28 | \[Battle\] Display Enemy HP | 1023 |
| 29 | \[Btl\]Enemy Flee Msg(Target... | 2005 |
| 30 | \[Battle\] Event on Game Over | 1024 |
| 31 | \[Battle\] Attack Multiplier | 1025 |
| 32 | \[Battle\] Defense Multiplier | 1026 |
| 33 | \[Battle\] Critical Hit Damage | 1027 |
| 34 | \[Battle\] Critical Hit Resistance | 1028 |

## Variable DB type 0: Allies

| Field | Label | Observed storage code |
| --- | --- | --- |
| 0 | Character Name | 2000 |
| 1 | Title | 2001 |
| 2 | Character Sprite | 2002 |
| 3 | Portrait \[Battle/Status\] | 2003 |
| 4 | Level | 1000 |
| 5 | Max Level | 1001 |
| 6 | HP | 1002 |
| 7 | Max HP | 1003 |
| 8 | SP | 1004 |
| 9 | Max SP | 1005 |
| 10 | Base Attack | 1006 |
| 11 | Base Defense | 1007 |
| 12 | Base Magic Attack | 1008 |
| 13 | Base Magic Defense | 1009 |
| 14 | Base Agility | 1010 |
| 15 | Base Accuracy \[%\] | 1011 |
| 16 | Base Evasion \[%\] | 1012 |
| 17 | Base Critical Rate \[%\] | 1013 |
| 18 | \[Growth\] Max HP Add /1Lv | 1014 |
| 19 | \[Growth\] Max SP Add /1Lv | 1015 |
| 20 | \[Growth\] Attack Add /1Lv | 1016 |
| 21 | \[Growth\] Defense Add /1Lv | 1017 |
| 22 | \[Growth\] Magic Atk Add /1Lv | 1018 |
| 23 | \[Growth\] Magic Def Add /1Lv | 1019 |
| 24 | \[Growth\] Agility Add /1Lv | 1020 |
| 25 | \[Growth\] Accuracy Add /1Lv | 1021 |
| 26 | \[Growth\] Evasion Add /1Lv | 1022 |
| 27 | \[Growth\] Critical Rt Add /1Lv | 1023 |
| 28 | Equipped Weapon | 1024 |
| 29 | Equipped Armor 1 | 1025 |
| 30 | Equipped Armor 2 | 1026 |
| 31 | Equipped Armor 3 | 1027 |
| 32 | Equipped Armor 4 | 1028 |
| 33 | Equipped Armor 5 | 1029 |
| 34 | Equipped Armor 6 | 1030 |
| 35 | Equipped Armor 7 | 1031 |
| 36 | Equippable Type 1 | 1032 |
| 37 | Equippable Type 2 | 1033 |
| 38 | Equippable Type 3 | 1034 |
| 39 | Equippable Type 4 | 1035 |
| 40 | Equippable Type 5 | 1036 |
| 41 | Equippable Type 6 | 1037 |
| 42 | Equippable Type 7 | 1038 |
| 43 | Equippable Type 8 | 1039 |
| 44 | Equippable Type 9 | 1040 |
| 45 | Equippable Type 10 | 1041 |
| 46 | \[Command 1\] | 1042 |
| 47 | \[Command 2\] | 1043 |
| 48 | \[Command 3\] | 1044 |
| 49 | \[Command 4\] | 1045 |
| 50 | \[Command 5\] | 1046 |
| 51 | \[Command 6\] | 1047 |
| 52 | \[Command 7\] | 1048 |
| 53 | \[Command 8\] | 1049 |
| 54 | Current Level EXP | 1050 |
| 55 | Current Level Required EXP | 1051 |
| 56 | Required EXP Incr Rate \[%\] | 1052 |
| 57 | Required EXP Incr\[FixedValue\] | 1053 |
| 58 | Auto-Act with AI? | 1054 |

## Variable DB type 1: ┣ Skill Learning Lv

| Field | Label | Observed storage code |
| --- | --- | --- |
| 0 | &lt;Skill&gt; Learning Level | 1000 |
| 1 | ┗ Skill to Learn | 1001 |
| 2 | &lt;Skill&gt; Learning Level | 1002 |
| 3 | ┗ Skill to Learn | 1003 |
| 4 | &lt;Skill&gt; Learning Level | 1004 |
| 5 | ┗ Skill to Learn | 1005 |
| 6 | &lt;Skill&gt; Learning Level | 1006 |
| 7 | ┗ Skill to Learn | 1007 |
| 8 | &lt;Skill&gt; Learning Level | 1008 |
| 9 | ┗ Skill to Learn | 1009 |
| 10 | &lt;Skill&gt; Learning Level | 1010 |
| 11 | ┗ Skill to Learn | 1011 |
| 12 | &lt;Skill&gt; Learning Level | 1012 |
| 13 | ┗ Skill to Learn | 1013 |
| 14 | &lt;Skill&gt; Learning Level | 1014 |
| 15 | ┗ Skill to Learn | 1015 |
| 16 | &lt;Skill&gt; Learning Level | 1016 |
| 17 | ┗ Skill to Learn | 1017 |
| 18 | &lt;Skill&gt; Learning Level | 1018 |
| 19 | ┗ Skill to Learn | 1019 |
| 20 | &lt;Skill&gt; Learning Level | 1020 |
| 21 | ┗ Skill to Learn | 1021 |
| 22 | &lt;Skill&gt; Learning Level | 1022 |
| 23 | ┗ Skill to Learn | 1023 |
| 24 | &lt;Skill&gt; Learning Level | 1024 |
| 25 | ┗ Skill to Learn | 1025 |
| 26 | &lt;Skill&gt; Learning Level | 1026 |
| 27 | ┗ Skill to Learn | 1027 |
| 28 | &lt;Skill&gt; Learning Level | 1028 |
| 29 | ┗ Skill to Learn | 1029 |
| 30 | &lt;Skill&gt; Learning Level | 1030 |
| 31 | ┗ Skill to Learn | 1031 |
| 32 | &lt;Skill&gt; Learning Level | 1032 |
| 33 | ┗ Skill to Learn | 1033 |
| 34 | &lt;Skill&gt; Learning Level | 1034 |
| 35 | ┗ Skill to Learn | 1035 |
| 36 | &lt;Skill&gt; Learning Level | 1036 |
| 37 | ┗ Skill to Learn | 1037 |
| 38 | &lt;Skill&gt; Learning Level | 1038 |
| 39 | ┗ Skill to Learn | 1039 |
| 40 | &lt;Skill&gt; Learning Level | 1040 |
| 41 | ┗ Skill to Learn | 1041 |
| 42 | &lt;Skill&gt; Learning Level | 1042 |
| 43 | ┗ Skill to Learn | 1043 |
| 44 | &lt;Skill&gt; Learning Level | 1044 |
| 45 | ┗ Skill to Learn | 1045 |
| 46 | &lt;Skill&gt; Learning Level | 1046 |
| 47 | ┗ Skill to Learn | 1047 |
| 48 | &lt;Skill&gt; Learning Level | 1048 |
| 49 | ┗ Skill to Learn | 1049 |
| 50 | &lt;Skill&gt; Learning Level | 1050 |
| 51 | ┗ Skill to Learn | 1051 |
| 52 | &lt;Skill&gt; Learning Level | 1052 |
| 53 | ┗ Skill to Learn | 1053 |
| 54 | &lt;Skill&gt; Learning Level | 1054 |
| 55 | ┗ Skill to Learn | 1055 |
| 56 | &lt;Skill&gt; Learning Level | 1056 |
| 57 | ┗ Skill to Learn | 1057 |
| 58 | &lt;Skill&gt; Learning Level | 1058 |
| 59 | ┗ Skill to Learn | 1059 |
| 60 | &lt;Skill&gt; Learning Level | 1060 |
| 61 | ┗ Skill to Learn | 1061 |
| 62 | &lt;Skill&gt; Learning Level | 1062 |
| 63 | ┗ Skill to Learn | 1063 |
| 64 | &lt;Skill&gt; Learning Level | 1064 |
| 65 | ┗ Skill to Learn | 1065 |
| 66 | &lt;Skill&gt; Learning Level | 1066 |
| 67 | ┗ Skill to Learn | 1067 |
| 68 | &lt;Skill&gt; Learning Level | 1068 |
| 69 | ┗ Skill to Learn | 1069 |
| 70 | &lt;Skill&gt; Learning Level | 1070 |
| 71 | ┗ Skill to Learn | 1071 |
| 72 | &lt;Skill&gt; Learning Level | 1072 |
| 73 | ┗ Skill to Learn | 1073 |
| 74 | &lt;Skill&gt; Learning Level | 1074 |
| 75 | ┗ Skill to Learn | 1075 |
| 76 | &lt;Skill&gt; Learning Level | 1076 |
| 77 | ┗ Skill to Learn | 1077 |
| 78 | &lt;Skill&gt; Learning Level | 1078 |
| 79 | ┗ Skill to Learn | 1079 |
| 80 | &lt;Skill&gt; Learning Level | 1080 |
| 81 | ┗ Skill to Learn | 1081 |
| 82 | &lt;Skill&gt; Learning Level | 1082 |
| 83 | ┗ Skill to Learn | 1083 |
| 84 | &lt;Skill&gt; Learning Level | 1084 |
| 85 | ┗ Skill to Learn | 1085 |
| 86 | &lt;Skill&gt; Learning Level | 1086 |
| 87 | ┗ Skill to Learn | 1087 |
| 88 | &lt;Skill&gt; Learning Level | 1088 |
| 89 | ┗ Skill to Learn | 1089 |
| 90 | &lt;Skill&gt; Learning Level | 1090 |
| 91 | ┗ Skill to Learn | 1091 |
| 92 | &lt;Skill&gt; Learning Level | 1092 |
| 93 | ┗ Skill to Learn | 1093 |
| 94 | &lt;Skill&gt; Learning Level | 1094 |
| 95 | ┗ Skill to Learn | 1095 |
| 96 | &lt;Skill&gt; Learning Level | 1096 |
| 97 | ┗ Skill to Learn | 1097 |
| 98 | &lt;Skill&gt; Learning Level | 1098 |
| 99 | ┗ Skill to Learn | 1099 |

## Variable DB type 2: ┣ Ally Action AI

| Field | Label | Observed storage code |
| --- | --- | --- |
| 0 | &lt;Action 1&gt; Condition ▼▼▼   | 1000 |
| 1 | ┣1 Target of Use \[If 1 Target\]   | 1001 |
| 2 | ┣1 Action to Perform               | 1002 |
| 3 | ┗1 When Condition Isn't Met | 1003 |
| 4 | &lt;Action 2&gt; Condition ▼▼▼   | 1004 |
| 5 | ┣2 Target of Use \[If 1 Target\]   | 1005 |
| 6 | ┣2 Action to Perform               | 1006 |
| 7 | ┗2 When Condition Isn't Met | 1007 |
| 8 | &lt;Action 3&gt; Condition ▼▼▼   | 1008 |
| 9 | ┣3 Target of Use \[If 1 Target\]   | 1009 |
| 10 | ┣3 Action to Perform               | 1010 |
| 11 | ┗3 When Condition Isn't Met | 1011 |
| 12 | &lt;Action 4&gt; Condition ▼▼▼   | 1012 |
| 13 | ┣4 Target of Use \[If 1 Target\]   | 1013 |
| 14 | ┣4 Action to Perform               | 1014 |
| 15 | ┗4 When Condition Isn't Met | 1015 |
| 16 | &lt;Action 5&gt; Condition ▼▼▼   | 1016 |
| 17 | ┣5 Target of Use \[If 1 Target\]   | 1017 |
| 18 | ┣5 Action to Perform               | 1018 |
| 19 | ┗5 When Condition Isn't Met | 1019 |
| 20 | &lt;Action 6&gt; Condition ▼▼▼   | 1020 |
| 21 | ┣6 Target of Use \[If 1 Target\]   | 1021 |
| 22 | ┣6 Action to Perform               | 1022 |
| 23 | ┗6 When Condition Isn't Met | 1023 |
| 24 | &lt;Action 7&gt; Condition ▼▼▼   | 1024 |
| 25 | ┣7 Target of Use \[If 1 Target\]   | 1025 |
| 26 | ┣7 Action to Perform               | 1026 |
| 27 | ┗7 When Condition Isn't Met | 1027 |
| 28 | &lt;Action 8&gt; Condition ▼▼▼   | 1028 |
| 29 | ┣8 Target of Use \[If 1 Target\]   | 1029 |
| 30 | ┣8 Action to Perform               | 1030 |
| 31 | ┗8 When Condition Isn't Met | 1031 |
| 32 | &lt;Action 9&gt; Condition ▼▼▼   | 1032 |
| 33 | ┣9 Target of Use \[If 1 Target\]   | 1033 |
| 34 | ┣9 Action to Perform               | 1034 |
| 35 | ┗9 When Condition Isn't Met | 1035 |
| 36 | &lt;Action 10&gt; Condition ▼▼▼ | 1036 |
| 37 | ┣10 Target of Use \[If 1 Target\]  | 1037 |
| 38 | ┣10 Action to Perform              | 1038 |
| 39 | ┗10 When Condition Isn't Met | 1039 |
| 40 | &lt;Action 11&gt; Condition ▼▼▼ | 1040 |
| 41 | ┣11 Target of Use \[If 1 Target\]  | 1041 |
| 42 | ┣11 Action to Perform              | 1042 |
| 43 | ┗11 When Condition Isn't Met | 1043 |
| 44 | &lt;Action 12&gt; Condition ▼▼▼ | 1044 |
| 45 | ┣12 Target of Use \[If 1 Target\]  | 1045 |
| 46 | ┣12 Action to Perform              | 1046 |
| 47 | ┗12 When Condition Isn't Met | 1047 |

## Variable DB type 3: ┣ Element Resistances

| Field | Label | Observed storage code |
| --- | --- | --- |
| 0 | &lt;\\udb\[7:\\d\[0\]\]&gt;Effect\[%\] | 1000 |
| 1 | &lt;\\udb\[7:\\d\[0\]\]&gt;Effect\[%\] | 1001 |
| 2 | &lt;\\udb\[7:\\d\[0\]\]&gt;Effect\[%\] | 1002 |
| 3 | &lt;\\udb\[7:\\d\[0\]\]&gt;Effect\[%\] | 1003 |
| 4 | &lt;\\udb\[7:\\d\[0\]\]&gt;Effect\[%\] | 1004 |
| 5 | &lt;\\udb\[7:\\d\[0\]\]&gt;Effect\[%\] | 1005 |
| 6 | &lt;\\udb\[7:\\d\[0\]\]&gt;Effect\[%\] | 1006 |
| 7 | &lt;\\udb\[7:\\d\[0\]\]&gt;Effect\[%\] | 1007 |
| 8 | &lt;\\udb\[7:\\d\[0\]\]&gt;Effect\[%\] | 1008 |
| 9 | &lt;\\udb\[7:\\d\[0\]\]&gt;Effect\[%\] | 1009 |
| 10 | &lt;\\udb\[7:\\d\[0\]\]&gt;Effect\[%\] | 1010 |
| 11 | &lt;\\udb\[7:\\d\[0\]\]&gt;Effect\[%\] | 1011 |
| 12 | &lt;\\udb\[7:\\d\[0\]\]&gt;Effect\[%\] | 1012 |
| 13 | &lt;\\udb\[7:\\d\[0\]\]&gt;Effect\[%\] | 1013 |
| 14 | &lt;\\udb\[7:\\d\[0\]\]&gt;Effect\[%\] | 1014 |
| 15 | &lt;\\udb\[7:\\d\[0\]\]&gt;Effect\[%\] | 1015 |
| 16 | &lt;\\udb\[7:\\d\[0\]\]&gt;Effect\[%\] | 1016 |
| 17 | &lt;\\udb\[7:\\d\[0\]\]&gt;Effect\[%\] | 1017 |
| 18 | &lt;\\udb\[7:\\d\[0\]\]&gt;Effect\[%\] | 1018 |
| 19 | &lt;\\udb\[7:\\d\[0\]\]&gt;Effect\[%\] | 1019 |
| 20 | &lt;\\udb\[7:\\d\[0\]\]&gt;Effect\[%\] | 1020 |
| 21 | &lt;\\udb\[7:\\d\[0\]\]&gt;Effect\[%\] | 1021 |
| 22 | &lt;\\udb\[7:\\d\[0\]\]&gt;Effect\[%\] | 1022 |
| 23 | &lt;\\udb\[7:\\d\[0\]\]&gt;Effect\[%\] | 1023 |
| 24 | &lt;\\udb\[7:\\d\[0\]\]&gt;Effect\[%\] | 1024 |
| 25 | &lt;\\udb\[7:\\d\[0\]\]&gt;Effect\[%\] | 1025 |
| 26 | &lt;\\udb\[7:\\d\[0\]\]&gt;Effect\[%\] | 1026 |
| 27 | &lt;\\udb\[7:\\d\[0\]\]&gt;Effect\[%\] | 1027 |
| 28 | &lt;\\udb\[7:\\d\[0\]\]&gt;Effect\[%\] | 1028 |
| 29 | &lt;\\udb\[7:\\d\[0\]\]&gt;Effect\[%\] | 1029 |
| 30 | &lt;\\udb\[7:\\d\[0\]\]&gt;Effect\[%\] | 1030 |
| 31 | &lt;\\udb\[7:\\d\[0\]\]&gt;Effect\[%\] | 1031 |
| 32 | &lt;\\udb\[7:\\d\[0\]\]&gt;Effect\[%\] | 1032 |
| 33 | &lt;\\udb\[7:\\d\[0\]\]&gt;Effect\[%\] | 1033 |
| 34 | &lt;\\udb\[7:\\d\[0\]\]&gt;Effect\[%\] | 1034 |
| 35 | &lt;\\udb\[7:\\d\[0\]\]&gt;Effect\[%\] | 1035 |
| 36 | &lt;\\udb\[7:\\d\[0\]\]&gt;Effect\[%\] | 1036 |
| 37 | &lt;\\udb\[7:\\d\[0\]\]&gt;Effect\[%\] | 1037 |
| 38 | &lt;\\udb\[7:\\d\[0\]\]&gt;Effect\[%\] | 1038 |
| 39 | &lt;\\udb\[7:\\d\[0\]\]&gt;Effect\[%\] | 1039 |
| 40 | &lt;\\udb\[7:\\d\[0\]\]&gt;Effect\[%\] | 1040 |
| 41 | &lt;\\udb\[7:\\d\[0\]\]&gt;Effect\[%\] | 1041 |
| 42 | &lt;\\udb\[7:\\d\[0\]\]&gt;Effect\[%\] | 1042 |
| 43 | &lt;\\udb\[7:\\d\[0\]\]&gt;Effect\[%\] | 1043 |
| 44 | &lt;\\udb\[7:\\d\[0\]\]&gt;Effect\[%\] | 1044 |
| 45 | &lt;\\udb\[7:\\d\[0\]\]&gt;Effect\[%\] | 1045 |
| 46 | &lt;\\udb\[7:\\d\[0\]\]&gt;Effect\[%\] | 1046 |
| 47 | &lt;\\udb\[7:\\d\[0\]\]&gt;Effect\[%\] | 1047 |
| 48 | &lt;\\udb\[7:\\d\[0\]\]&gt;Effect\[%\] | 1048 |
| 49 | &lt;\\udb\[7:\\d\[0\]\]&gt;Effect\[%\] | 1049 |
| 50 | &lt;\\udb\[7:\\d\[0\]\]&gt;Effect\[%\] | 1050 |
| 51 | &lt;\\udb\[7:\\d\[0\]\]&gt;Effect\[%\] | 1051 |
| 52 | &lt;\\udb\[7:\\d\[0\]\]&gt;Effect\[%\] | 1052 |
| 53 | &lt;\\udb\[7:\\d\[0\]\]&gt;Effect\[%\] | 1053 |
| 54 | &lt;\\udb\[7:\\d\[0\]\]&gt;Effect\[%\] | 1054 |
| 55 | &lt;\\udb\[7:\\d\[0\]\]&gt;Effect\[%\] | 1055 |
| 56 | &lt;\\udb\[7:\\d\[0\]\]&gt;Effect\[%\] | 1056 |
| 57 | &lt;\\udb\[7:\\d\[0\]\]&gt;Effect\[%\] | 1057 |
| 58 | &lt;\\udb\[7:\\d\[0\]\]&gt;Effect\[%\] | 1058 |
| 59 | &lt;\\udb\[7:\\d\[0\]\]&gt;Effect\[%\] | 1059 |
| 60 | &lt;\\udb\[7:\\d\[0\]\]&gt;Effect\[%\] | 1060 |
| 61 | &lt;\\udb\[7:\\d\[0\]\]&gt;Effect\[%\] | 1061 |
| 62 | &lt;\\udb\[7:\\d\[0\]\]&gt;Effect\[%\] | 1062 |
| 63 | &lt;\\udb\[7:\\d\[0\]\]&gt;Effect\[%\] | 1063 |
| 64 | &lt;\\udb\[7:\\d\[0\]\]&gt;Effect\[%\] | 1064 |
| 65 | &lt;\\udb\[7:\\d\[0\]\]&gt;Effect\[%\] | 1065 |
| 66 | &lt;\\udb\[7:\\d\[0\]\]&gt;Effect\[%\] | 1066 |
| 67 | &lt;\\udb\[7:\\d\[0\]\]&gt;Effect\[%\] | 1067 |
| 68 | &lt;\\udb\[7:\\d\[0\]\]&gt;Effect\[%\] | 1068 |
| 69 | &lt;\\udb\[7:\\d\[0\]\]&gt;Effect\[%\] | 1069 |
| 70 | &lt;\\udb\[7:\\d\[0\]\]&gt;Effect\[%\] | 1070 |
| 71 | &lt;\\udb\[7:\\d\[0\]\]&gt;Effect\[%\] | 1071 |
| 72 | &lt;\\udb\[7:\\d\[0\]\]&gt;Effect\[%\] | 1072 |
| 73 | &lt;\\udb\[7:\\d\[0\]\]&gt;Effect\[%\] | 1073 |
| 74 | &lt;\\udb\[7:\\d\[0\]\]&gt;Effect\[%\] | 1074 |
| 75 | &lt;\\udb\[7:\\d\[0\]\]&gt;Effect\[%\] | 1075 |
| 76 | &lt;\\udb\[7:\\d\[0\]\]&gt;Effect\[%\] | 1076 |
| 77 | &lt;\\udb\[7:\\d\[0\]\]&gt;Effect\[%\] | 1077 |
| 78 | &lt;\\udb\[7:\\d\[0\]\]&gt;Effect\[%\] | 1078 |
| 79 | &lt;\\udb\[7:\\d\[0\]\]&gt;Effect\[%\] | 1079 |
| 80 | &lt;\\udb\[7:\\d\[0\]\]&gt;Effect\[%\] | 1080 |
| 81 | &lt;\\udb\[7:\\d\[0\]\]&gt;Effect\[%\] | 1081 |
| 82 | &lt;\\udb\[7:\\d\[0\]\]&gt;Effect\[%\] | 1082 |
| 83 | &lt;\\udb\[7:\\d\[0\]\]&gt;Effect\[%\] | 1083 |
| 84 | &lt;\\udb\[7:\\d\[0\]\]&gt;Effect\[%\] | 1084 |
| 85 | &lt;\\udb\[7:\\d\[0\]\]&gt;Effect\[%\] | 1085 |
| 86 | &lt;\\udb\[7:\\d\[0\]\]&gt;Effect\[%\] | 1086 |
| 87 | &lt;\\udb\[7:\\d\[0\]\]&gt;Effect\[%\] | 1087 |
| 88 | &lt;\\udb\[7:\\d\[0\]\]&gt;Effect\[%\] | 1088 |
| 89 | &lt;\\udb\[7:\\d\[0\]\]&gt;Effect\[%\] | 1089 |
| 90 | &lt;\\udb\[7:\\d\[0\]\]&gt;Effect\[%\] | 1090 |
| 91 | &lt;\\udb\[7:\\d\[0\]\]&gt;Effect\[%\] | 1091 |
| 92 | &lt;\\udb\[7:\\d\[0\]\]&gt;Effect\[%\] | 1092 |
| 93 | &lt;\\udb\[7:\\d\[0\]\]&gt;Effect\[%\] | 1093 |
| 94 | &lt;\\udb\[7:\\d\[0\]\]&gt;Effect\[%\] | 1094 |
| 95 | &lt;\\udb\[7:\\d\[0\]\]&gt;Effect\[%\] | 1095 |
| 96 | &lt;\\udb\[7:\\d\[0\]\]&gt;Effect\[%\] | 1096 |
| 97 | &lt;\\udb\[7:\\d\[0\]\]&gt;Effect\[%\] | 1097 |
| 98 | &lt;\\udb\[7:\\d\[0\]\]&gt;Effect\[%\] | 1098 |
| 99 | &lt;\\udb\[7:\\d\[0\]\]&gt;Effect\[%\] | 1099 |

## Variable DB type 4: ┣ State Resistances

| Field | Label | Observed storage code |
| --- | --- | --- |
| 0 | &lt;\\udb\[8:\\d\[0\]\]&gt;S. Rate | 1000 |
| 1 | &lt;\\udb\[8:\\d\[0\]\]&gt;S. Rate | 1001 |
| 2 | &lt;\\udb\[8:\\d\[0\]\]&gt;S. Rate | 1002 |
| 3 | &lt;\\udb\[8:\\d\[0\]\]&gt;S. Rate | 1003 |
| 4 | &lt;\\udb\[8:\\d\[0\]\]&gt;S. Rate | 1004 |
| 5 | &lt;\\udb\[8:\\d\[0\]\]&gt;S. Rate | 1005 |
| 6 | &lt;\\udb\[8:\\d\[0\]\]&gt;S. Rate | 1006 |
| 7 | &lt;\\udb\[8:\\d\[0\]\]&gt;S. Rate | 1007 |
| 8 | &lt;\\udb\[8:\\d\[0\]\]&gt;S. Rate | 1008 |
| 9 | &lt;\\udb\[8:\\d\[0\]\]&gt;S. Rate | 1009 |
| 10 | &lt;\\udb\[8:\\d\[0\]\]&gt;S. Rate | 1010 |
| 11 | &lt;\\udb\[8:\\d\[0\]\]&gt;S. Rate | 1011 |
| 12 | &lt;\\udb\[8:\\d\[0\]\]&gt;S. Rate | 1012 |
| 13 | &lt;\\udb\[8:\\d\[0\]\]&gt;S. Rate | 1013 |
| 14 | &lt;\\udb\[8:\\d\[0\]\]&gt;S. Rate | 1014 |
| 15 | &lt;\\udb\[8:\\d\[0\]\]&gt;S. Rate | 1015 |
| 16 | &lt;\\udb\[8:\\d\[0\]\]&gt;S. Rate | 1016 |
| 17 | &lt;\\udb\[8:\\d\[0\]\]&gt;S. Rate | 1017 |
| 18 | &lt;\\udb\[8:\\d\[0\]\]&gt;S. Rate | 1018 |
| 19 | &lt;\\udb\[8:\\d\[0\]\]&gt;S. Rate | 1019 |
| 20 | &lt;\\udb\[8:\\d\[0\]\]&gt;S. Rate | 1020 |
| 21 | &lt;\\udb\[8:\\d\[0\]\]&gt;S. Rate | 1021 |
| 22 | &lt;\\udb\[8:\\d\[0\]\]&gt;S. Rate | 1022 |
| 23 | &lt;\\udb\[8:\\d\[0\]\]&gt;S. Rate | 1023 |
| 24 | &lt;\\udb\[8:\\d\[0\]\]&gt;S. Rate | 1024 |
| 25 | &lt;\\udb\[8:\\d\[0\]\]&gt;S. Rate | 1025 |
| 26 | &lt;\\udb\[8:\\d\[0\]\]&gt;S. Rate | 1026 |
| 27 | &lt;\\udb\[8:\\d\[0\]\]&gt;S. Rate | 1027 |
| 28 | &lt;\\udb\[8:\\d\[0\]\]&gt;S. Rate | 1028 |
| 29 | &lt;\\udb\[8:\\d\[0\]\]&gt;S. Rate | 1029 |
| 30 | &lt;\\udb\[8:\\d\[0\]\]&gt;S. Rate | 1030 |
| 31 | &lt;\\udb\[8:\\d\[0\]\]&gt;S. Rate | 1031 |
| 32 | &lt;\\udb\[8:\\d\[0\]\]&gt;S. Rate | 1032 |
| 33 | &lt;\\udb\[8:\\d\[0\]\]&gt;S. Rate | 1033 |
| 34 | &lt;\\udb\[8:\\d\[0\]\]&gt;S. Rate | 1034 |
| 35 | &lt;\\udb\[8:\\d\[0\]\]&gt;S. Rate | 1035 |
| 36 | &lt;\\udb\[8:\\d\[0\]\]&gt;S. Rate | 1036 |
| 37 | &lt;\\udb\[8:\\d\[0\]\]&gt;S. Rate | 1037 |
| 38 | &lt;\\udb\[8:\\d\[0\]\]&gt;S. Rate | 1038 |
| 39 | &lt;\\udb\[8:\\d\[0\]\]&gt;S. Rate | 1039 |
| 40 | &lt;\\udb\[8:\\d\[0\]\]&gt;S. Rate | 1040 |
| 41 | &lt;\\udb\[8:\\d\[0\]\]&gt;S. Rate | 1041 |
| 42 | &lt;\\udb\[8:\\d\[0\]\]&gt;S. Rate | 1042 |
| 43 | &lt;\\udb\[8:\\d\[0\]\]&gt;S. Rate | 1043 |
| 44 | &lt;\\udb\[8:\\d\[0\]\]&gt;S. Rate | 1044 |
| 45 | &lt;\\udb\[8:\\d\[0\]\]&gt;S. Rate | 1045 |
| 46 | &lt;\\udb\[8:\\d\[0\]\]&gt;S. Rate | 1046 |
| 47 | &lt;\\udb\[8:\\d\[0\]\]&gt;S. Rate | 1047 |
| 48 | &lt;\\udb\[8:\\d\[0\]\]&gt;S. Rate | 1048 |
| 49 | &lt;\\udb\[8:\\d\[0\]\]&gt;S. Rate | 1049 |
| 50 | &lt;\\udb\[8:\\d\[0\]\]&gt;S. Rate | 1050 |
| 51 | &lt;\\udb\[8:\\d\[0\]\]&gt;S. Rate | 1051 |
| 52 | &lt;\\udb\[8:\\d\[0\]\]&gt;S. Rate | 1052 |
| 53 | &lt;\\udb\[8:\\d\[0\]\]&gt;S. Rate | 1053 |
| 54 | &lt;\\udb\[8:\\d\[0\]\]&gt;S. Rate | 1054 |
| 55 | &lt;\\udb\[8:\\d\[0\]\]&gt;S. Rate | 1055 |
| 56 | &lt;\\udb\[8:\\d\[0\]\]&gt;S. Rate | 1056 |
| 57 | &lt;\\udb\[8:\\d\[0\]\]&gt;S. Rate | 1057 |
| 58 | &lt;\\udb\[8:\\d\[0\]\]&gt;S. Rate | 1058 |
| 59 | &lt;\\udb\[8:\\d\[0\]\]&gt;S. Rate | 1059 |
| 60 | &lt;\\udb\[8:\\d\[0\]\]&gt;S. Rate | 1060 |
| 61 | &lt;\\udb\[8:\\d\[0\]\]&gt;S. Rate | 1061 |
| 62 | &lt;\\udb\[8:\\d\[0\]\]&gt;S. Rate | 1062 |
| 63 | &lt;\\udb\[8:\\d\[0\]\]&gt;S. Rate | 1063 |
| 64 | &lt;\\udb\[8:\\d\[0\]\]&gt;S. Rate | 1064 |
| 65 | &lt;\\udb\[8:\\d\[0\]\]&gt;S. Rate | 1065 |
| 66 | &lt;\\udb\[8:\\d\[0\]\]&gt;S. Rate | 1066 |
| 67 | &lt;\\udb\[8:\\d\[0\]\]&gt;S. Rate | 1067 |
| 68 | &lt;\\udb\[8:\\d\[0\]\]&gt;S. Rate | 1068 |
| 69 | &lt;\\udb\[8:\\d\[0\]\]&gt;S. Rate | 1069 |
| 70 | &lt;\\udb\[8:\\d\[0\]\]&gt;S. Rate | 1070 |
| 71 | &lt;\\udb\[8:\\d\[0\]\]&gt;S. Rate | 1071 |
| 72 | &lt;\\udb\[8:\\d\[0\]\]&gt;S. Rate | 1072 |
| 73 | &lt;\\udb\[8:\\d\[0\]\]&gt;S. Rate | 1073 |
| 74 | &lt;\\udb\[8:\\d\[0\]\]&gt;S. Rate | 1074 |
| 75 | &lt;\\udb\[8:\\d\[0\]\]&gt;S. Rate | 1075 |
| 76 | &lt;\\udb\[8:\\d\[0\]\]&gt;S. Rate | 1076 |
| 77 | &lt;\\udb\[8:\\d\[0\]\]&gt;S. Rate | 1077 |
| 78 | &lt;\\udb\[8:\\d\[0\]\]&gt;S. Rate | 1078 |
| 79 | &lt;\\udb\[8:\\d\[0\]\]&gt;S. Rate | 1079 |
| 80 | &lt;\\udb\[8:\\d\[0\]\]&gt;S. Rate | 1080 |
| 81 | &lt;\\udb\[8:\\d\[0\]\]&gt;S. Rate | 1081 |
| 82 | &lt;\\udb\[8:\\d\[0\]\]&gt;S. Rate | 1082 |
| 83 | &lt;\\udb\[8:\\d\[0\]\]&gt;S. Rate | 1083 |
| 84 | &lt;\\udb\[8:\\d\[0\]\]&gt;S. Rate | 1084 |
| 85 | &lt;\\udb\[8:\\d\[0\]\]&gt;S. Rate | 1085 |
| 86 | &lt;\\udb\[8:\\d\[0\]\]&gt;S. Rate | 1086 |
| 87 | &lt;\\udb\[8:\\d\[0\]\]&gt;S. Rate | 1087 |
| 88 | &lt;\\udb\[8:\\d\[0\]\]&gt;S. Rate | 1088 |
| 89 | &lt;\\udb\[8:\\d\[0\]\]&gt;S. Rate | 1089 |
| 90 | &lt;\\udb\[8:\\d\[0\]\]&gt;S. Rate | 1090 |
| 91 | &lt;\\udb\[8:\\d\[0\]\]&gt;S. Rate | 1091 |
| 92 | &lt;\\udb\[8:\\d\[0\]\]&gt;S. Rate | 1092 |
| 93 | &lt;\\udb\[8:\\d\[0\]\]&gt;S. Rate | 1093 |
| 94 | &lt;\\udb\[8:\\d\[0\]\]&gt;S. Rate | 1094 |
| 95 | &lt;\\udb\[8:\\d\[0\]\]&gt;S. Rate | 1095 |
| 96 | &lt;\\udb\[8:\\d\[0\]\]&gt;S. Rate | 1096 |
| 97 | &lt;\\udb\[8:\\d\[0\]\]&gt;S. Rate | 1097 |
| 98 | &lt;\\udb\[8:\\d\[0\]\]&gt;S. Rate | 1098 |
| 99 | &lt;\\udb\[8:\\d\[0\]\]&gt;S. Rate | 1099 |

## Variable DB type 5: ┗ State List

| Field | Label | Observed storage code |
| --- | --- | --- |
| 0 | \\udb\[8:0\] Steps Left | 1000 |
| 1 | \\udb\[8:1\] Steps Left | 1001 |
| 2 | \\udb\[8:2\] Steps Left | 1002 |
| 3 | \\udb\[8:3\] | 1003 |
| 4 | \\udb\[8:4\] | 1004 |
| 5 | \\udb\[8:5\] | 1005 |
| 6 | \\udb\[8:6\] | 1006 |
| 7 | \\udb\[8:7\] | 1007 |
| 8 | \\udb\[8:8\] | 1008 |
| 9 | \\udb\[8:9\] | 1009 |
| 10 | \\udb\[8:10\] | 1010 |
| 11 | \\udb\[8:11\] | 1011 |
| 12 | \\udb\[8:12\] | 1012 |
| 13 | \\udb\[8:13\] | 1013 |
| 14 | \\udb\[8:14\] | 1014 |
| 15 | \\udb\[8:15\] | 1015 |
| 16 | \\udb\[8:16\] | 1016 |
| 17 | \\udb\[8:17\] | 1017 |
| 18 | \\udb\[8:18\] | 1018 |
| 19 | \\udb\[8:19\] | 1019 |
| 20 |  | 1020 |
| 21 |  | 1021 |
| 22 |  | 1022 |
| 23 |  | 1023 |
| 24 |  | 1024 |
| 25 |  | 1025 |
| 26 |  | 1026 |
| 27 |  | 1027 |
| 28 |  | 1028 |
| 29 |  | 1029 |
| 30 |  | 1030 |
| 31 |  | 1031 |
| 32 |  | 1032 |
| 33 |  | 1033 |
| 34 |  | 1034 |
| 35 |  | 1035 |
| 36 |  | 1036 |
| 37 |  | 1037 |
| 38 |  | 1038 |
| 39 |  | 1039 |
| 40 |  | 1040 |
| 41 |  | 1041 |
| 42 |  | 1042 |
| 43 |  | 1043 |
| 44 |  | 1044 |
| 45 |  | 1045 |
| 46 |  | 1046 |
| 47 |  | 1047 |
| 48 |  | 1048 |
| 49 |  | 1049 |
| 50 |  | 1050 |
| 51 |  | 1051 |
| 52 |  | 1052 |
| 53 |  | 1053 |
| 54 |  | 1054 |
| 55 |  | 1055 |
| 56 |  | 1056 |
| 57 |  | 1057 |
| 58 |  | 1058 |
| 59 |  | 1059 |
| 60 |  | 1060 |
| 61 |  | 1061 |
| 62 |  | 1062 |
| 63 |  | 1063 |
| 64 |  | 1064 |
| 65 |  | 1065 |
| 66 |  | 1066 |
| 67 |  | 1067 |
| 68 |  | 1068 |
| 69 |  | 1069 |
| 70 |  | 1070 |
| 71 |  | 1071 |
| 72 |  | 1072 |
| 73 |  | 1073 |
| 74 |  | 1074 |
| 75 |  | 1075 |
| 76 |  | 1076 |
| 77 |  | 1077 |
| 78 |  | 1078 |
| 79 |  | 1079 |
| 80 |  | 1080 |
| 81 |  | 1081 |
| 82 |  | 1082 |
| 83 |  | 1083 |
| 84 |  | 1084 |
| 85 |  | 1085 |
| 86 |  | 1086 |
| 87 |  | 1087 |
| 88 |  | 1088 |
| 89 |  | 1089 |
| 90 |  | 1090 |
| 91 |  | 1091 |
| 92 |  | 1092 |
| 93 |  | 1093 |
| 94 |  | 1094 |
| 95 |  | 1095 |
| 96 |  | 1096 |
| 97 |  | 1097 |
| 98 |  | 1098 |
| 99 |  | 1099 |

## Variable DB type 6: Party

| Field | Label | Observed storage code |
| --- | --- | --- |
| 0 | Current Money | 1000 |
| 1 | Member 1 | 1001 |
| 2 | Member 2 | 1002 |
| 3 | Member 3 | 1003 |
| 4 | Member 4 | 1004 |
| 5 | Member 5 | 1005 |
| 6 | Member 6 | 1006 |

## Variable DB type 7: ┣ Owned Items

| Field | Label | Observed storage code |
| --- | --- | --- |
| 0 | Owned Quantity | 1000 |

## Variable DB type 8: ┣ Owned Weapons

| Field | Label | Observed storage code |
| --- | --- | --- |
| 0 | Owned Quantity | 1000 |

## Variable DB type 9: ┗ Owned Armors

| Field | Label | Observed storage code |
| --- | --- | --- |
| 0 | Owned Quantity | 1000 |

## Variable DB type 10: ×┏Battle Temp Status

| Field | Label | Observed storage code |
| --- | --- | --- |
| 0 | Character Name | 2000 |
| 1 | Image File | 2001 |
| 2 | Temp Overwrite Image File | 2002 |
| 3 | \[Fainted?\] | 1000 |
| 4 | Display Color ID | 1001 |
| 5 | HP | 1002 |
| 6 | Max HP | 1003 |
| 7 | SP | 1004 |
| 8 | Max SP | 1005 |
| 9 | Base Attack | 1006 |
| 10 | Base Defense | 1007 |
| 11 | Base Magic Attack | 1008 |
| 12 | Base Magic Defense | 1009 |
| 13 | Base Agility | 1010 |
| 14 | Base Accuracy \[%\] | 1011 |
| 15 | Base Evasion \[%\] | 1012 |
| 16 | Base Critical Rate \[%\] | 1013 |
| 17 | Character ID \[Enemy:10,000+\] | 1014 |
| 18 | Equipped Weapon | 1015 |
| 19 | Equipped Armor 1 | 1016 |
| 20 | Equipped Armor 2 | 1017 |
| 21 | Equipped Armor 3 | 1018 |
| 22 | Equipped Armor 4 | 1019 |
| 23 | Equipped Armor 5 | 1020 |
| 24 | Equipped Armor 6 | 1021 |
| 25 | Equipped Armor 7 | 1022 |
| 26 | \[Command 1\] | 1023 |
| 27 | \[Command 2\] | 1024 |
| 28 | \[Command 3\] | 1025 |
| 29 | \[Command 4\] | 1026 |
| 30 | \[Command 5\] | 1027 |
| 31 | \[Command 6\] | 1028 |
| 32 | \[Command 7\] | 1029 |
| 33 | \[Command 8\] | 1030 |
| 34 | Command 1 Usable Flag | 1031 |
| 35 | Command 2 Usable Flag | 1032 |
| 36 | Command 3 Usable Flag | 1033 |
| 37 | Command 4 Usable Flag | 1034 |
| 38 | Command 5 Usable Flag | 1035 |
| 39 | Command 6 Usable Flag | 1036 |
| 40 | Command 7 Usable Flag | 1037 |
| 41 | Command 8 Usable Flag | 1038 |
| 42 | \[Enemy\] EXP Reward | 1039 |
| 43 | \[Enemy\] Money Reward | 1040 |
| 44 | \[Temp\] Post-Calc Max HP | 1041 |
| 45 | \[Temp\] Equip Calc Max HP | 1042 |
| 46 | \[Temp\] Post-Calc Max SP | 1043 |
| 47 | \[Temp\] Equip Calc Max SP | 1044 |
| 48 | \[Temp\] Post-Calc Attack | 1045 |
| 49 | \[Temp\] Post-Calc Defense | 1046 |
| 50 | \[Temp\] Post-Calc Magic Atk | 1047 |
| 51 | \[Temp\] Post-Calc Magic Def | 1048 |
| 52 | \[Temp\] Post-Calc Agility | 1049 |
| 53 | \[Temp\] Post-Calc Accuracy | 1050 |
| 54 | \[Temp\] Post-Calc Evasion | 1051 |
| 55 | \[Temp\]Post-Calc Critical Rate | 1052 |
| 56 | \[Physical Dmg Taken Rate\] | 1053 |
| 57 | \[Magic Damage Taken Rate\] | 1054 |
| 58 | \[Target Level\] -1:NotTargeted | 1055 |
| 59 | \[Action Restriction\] | 1056 |
| 60 | \[Skill Limitation\] 1:Sealed | 1057 |
| 61 | \[Counterattack?\] | 1058 |
| 62 | HP Change per Turn \[%\] | 1059 |
| 63 | HP Change per Turn \[Fixed\] | 1060 |
| 64 | SP Change per Turn \[%\] | 1061 |
| 65 | SP Change per Turn \[Fixed\] | 1062 |
| 66 | \[Temp\] Weapon in Use | 1063 |
| 67 | Action Restriction Message | 2003 |
| 68 | Skill Limitation Message | 2004 |
| 69 | \[Temp\] State Names | 2005 |
| 70 | \[Store\] EXP/Item Get Flag | 1064 |
| 71 | \[Sto\] OldColor / EnemyDeadF | 1065 |
| 72 | \[Enemy\] Item Drop | 1066 |
| 73 | \[Enemy\] Item Drop Rate | 1067 |
| 74 | \[Enemy\] Weapon Drop | 1068 |
| 75 | \[Enemy\] Weapon Drop Rate | 1069 |
| 76 | \[Enemy\] Armor Drop | 1070 |
| 77 | \[Enemy\] Armor Drop Rate | 1071 |

## Variable DB type 11: ×┣Element Resist Calc

| Field | Label | Observed storage code |
| --- | --- | --- |
| 0 |  | 1000 |
| 1 |  | 1001 |
| 2 |  | 1002 |
| 3 |  | 1003 |
| 4 |  | 1004 |
| 5 |  | 1005 |
| 6 |  | 1006 |
| 7 |  | 1007 |
| 8 |  | 1008 |
| 9 |  | 1009 |
| 10 |  | 1010 |
| 11 |  | 1011 |
| 12 |  | 1012 |
| 13 |  | 1013 |
| 14 |  | 1014 |
| 15 |  | 1015 |
| 16 |  | 1016 |
| 17 |  | 1017 |
| 18 |  | 1018 |
| 19 |  | 1019 |
| 20 |  | 1020 |
| 21 |  | 1021 |
| 22 |  | 1022 |
| 23 |  | 1023 |
| 24 |  | 1024 |
| 25 |  | 1025 |
| 26 |  | 1026 |
| 27 |  | 1027 |
| 28 |  | 1028 |
| 29 |  | 1029 |
| 30 |  | 1030 |
| 31 |  | 1031 |
| 32 |  | 1032 |
| 33 |  | 1033 |
| 34 |  | 1034 |
| 35 |  | 1035 |
| 36 |  | 1036 |
| 37 |  | 1037 |
| 38 |  | 1038 |
| 39 |  | 1039 |
| 40 |  | 1040 |
| 41 |  | 1041 |
| 42 |  | 1042 |
| 43 |  | 1043 |
| 44 |  | 1044 |
| 45 |  | 1045 |
| 46 |  | 1046 |
| 47 |  | 1047 |
| 48 |  | 1048 |
| 49 |  | 1049 |
| 50 |  | 1050 |
| 51 |  | 1051 |
| 52 |  | 1052 |
| 53 |  | 1053 |
| 54 |  | 1054 |
| 55 |  | 1055 |
| 56 |  | 1056 |
| 57 |  | 1057 |
| 58 |  | 1058 |
| 59 |  | 1059 |
| 60 |  | 1060 |
| 61 |  | 1061 |
| 62 |  | 1062 |
| 63 |  | 1063 |
| 64 |  | 1064 |
| 65 |  | 1065 |
| 66 |  | 1066 |
| 67 |  | 1067 |
| 68 |  | 1068 |
| 69 |  | 1069 |
| 70 |  | 1070 |
| 71 |  | 1071 |
| 72 |  | 1072 |
| 73 |  | 1073 |
| 74 |  | 1074 |
| 75 |  | 1075 |
| 76 |  | 1076 |
| 77 |  | 1077 |
| 78 |  | 1078 |
| 79 |  | 1079 |
| 80 |  | 1080 |
| 81 |  | 1081 |
| 82 |  | 1082 |
| 83 |  | 1083 |
| 84 |  | 1084 |
| 85 |  | 1085 |
| 86 |  | 1086 |
| 87 |  | 1087 |
| 88 |  | 1088 |
| 89 |  | 1089 |
| 90 |  | 1090 |
| 91 |  | 1091 |
| 92 |  | 1092 |
| 93 |  | 1093 |
| 94 |  | 1094 |
| 95 |  | 1095 |
| 96 |  | 1096 |
| 97 |  | 1097 |
| 98 |  | 1098 |
| 99 |  | 1099 |

## Variable DB type 12: ×┣State Resist Calc

| Field | Label | Observed storage code |
| --- | --- | --- |
| 0 |  | 1000 |
| 1 |  | 1001 |
| 2 |  | 1002 |
| 3 |  | 1003 |
| 4 |  | 1004 |
| 5 |  | 1005 |
| 6 |  | 1006 |
| 7 |  | 1007 |
| 8 |  | 1008 |
| 9 |  | 1009 |
| 10 |  | 1010 |
| 11 |  | 1011 |
| 12 |  | 1012 |
| 13 |  | 1013 |
| 14 |  | 1014 |
| 15 |  | 1015 |
| 16 |  | 1016 |
| 17 |  | 1017 |
| 18 |  | 1018 |
| 19 |  | 1019 |
| 20 |  | 1020 |
| 21 |  | 1021 |
| 22 |  | 1022 |
| 23 |  | 1023 |
| 24 |  | 1024 |
| 25 |  | 1025 |
| 26 |  | 1026 |
| 27 |  | 1027 |
| 28 |  | 1028 |
| 29 |  | 1029 |
| 30 |  | 1030 |
| 31 |  | 1031 |
| 32 |  | 1032 |
| 33 |  | 1033 |
| 34 |  | 1034 |
| 35 |  | 1035 |
| 36 |  | 1036 |
| 37 |  | 1037 |
| 38 |  | 1038 |
| 39 |  | 1039 |
| 40 |  | 1040 |
| 41 |  | 1041 |
| 42 |  | 1042 |
| 43 |  | 1043 |
| 44 |  | 1044 |
| 45 |  | 1045 |
| 46 |  | 1046 |
| 47 |  | 1047 |
| 48 |  | 1048 |
| 49 |  | 1049 |
| 50 |  | 1050 |
| 51 |  | 1051 |
| 52 |  | 1052 |
| 53 |  | 1053 |
| 54 |  | 1054 |
| 55 |  | 1055 |
| 56 |  | 1056 |
| 57 |  | 1057 |
| 58 |  | 1058 |
| 59 |  | 1059 |
| 60 |  | 1060 |
| 61 |  | 1061 |
| 62 |  | 1062 |
| 63 |  | 1063 |
| 64 |  | 1064 |
| 65 |  | 1065 |
| 66 |  | 1066 |
| 67 |  | 1067 |
| 68 |  | 1068 |
| 69 |  | 1069 |
| 70 |  | 1070 |
| 71 |  | 1071 |
| 72 |  | 1072 |
| 73 |  | 1073 |
| 74 |  | 1074 |
| 75 |  | 1075 |
| 76 |  | 1076 |
| 77 |  | 1077 |
| 78 |  | 1078 |
| 79 |  | 1079 |
| 80 |  | 1080 |
| 81 |  | 1081 |
| 82 |  | 1082 |
| 83 |  | 1083 |
| 84 |  | 1084 |
| 85 |  | 1085 |
| 86 |  | 1086 |
| 87 |  | 1087 |
| 88 |  | 1088 |
| 89 |  | 1089 |
| 90 |  | 1090 |
| 91 |  | 1091 |
| 92 |  | 1092 |
| 93 |  | 1093 |
| 94 |  | 1094 |
| 95 |  | 1095 |
| 96 |  | 1096 |
| 97 |  | 1097 |
| 98 |  | 1098 |
| 99 |  | 1099 |

## Variable DB type 13: ×┣State List

| Field | Label | Observed storage code |
| --- | --- | --- |
| 0 | \\udb\[8:0\] Turns Left | 1000 |
| 1 | \\udb\[8:1\] Turns Left | 1001 |
| 2 | \\udb\[8:2\] Turns Left | 1002 |
| 3 | ...Rest Omitted | 1003 |
| 4 |  | 1004 |
| 5 |  | 1005 |
| 6 |  | 1006 |
| 7 |  | 1007 |
| 8 |  | 1008 |
| 9 |  | 1009 |
| 10 |  | 1010 |
| 11 |  | 1011 |
| 12 |  | 1012 |
| 13 |  | 1013 |
| 14 |  | 1014 |
| 15 |  | 1015 |
| 16 |  | 1016 |
| 17 |  | 1017 |
| 18 |  | 1018 |
| 19 |  | 1019 |
| 20 |  | 1020 |
| 21 |  | 1021 |
| 22 |  | 1022 |
| 23 |  | 1023 |
| 24 |  | 1024 |
| 25 |  | 1025 |
| 26 |  | 1026 |
| 27 |  | 1027 |
| 28 |  | 1028 |
| 29 |  | 1029 |
| 30 |  | 1030 |
| 31 |  | 1031 |
| 32 |  | 1032 |
| 33 |  | 1033 |
| 34 |  | 1034 |
| 35 |  | 1035 |
| 36 |  | 1036 |
| 37 |  | 1037 |
| 38 |  | 1038 |
| 39 |  | 1039 |
| 40 |  | 1040 |
| 41 |  | 1041 |
| 42 |  | 1042 |
| 43 |  | 1043 |
| 44 |  | 1044 |
| 45 |  | 1045 |
| 46 |  | 1046 |
| 47 |  | 1047 |
| 48 |  | 1048 |
| 49 |  | 1049 |
| 50 |  | 1050 |
| 51 |  | 1051 |
| 52 |  | 1052 |
| 53 |  | 1053 |
| 54 |  | 1054 |
| 55 |  | 1055 |
| 56 |  | 1056 |
| 57 |  | 1057 |
| 58 |  | 1058 |
| 59 |  | 1059 |
| 60 |  | 1060 |
| 61 |  | 1061 |
| 62 |  | 1062 |
| 63 |  | 1063 |
| 64 |  | 1064 |
| 65 |  | 1065 |
| 66 |  | 1066 |
| 67 |  | 1067 |
| 68 |  | 1068 |
| 69 |  | 1069 |
| 70 |  | 1070 |
| 71 |  | 1071 |
| 72 |  | 1072 |
| 73 |  | 1073 |
| 74 |  | 1074 |
| 75 |  | 1075 |
| 76 |  | 1076 |
| 77 |  | 1077 |
| 78 |  | 1078 |
| 79 |  | 1079 |
| 80 |  | 1080 |
| 81 |  | 1081 |
| 82 |  | 1082 |
| 83 |  | 1083 |
| 84 |  | 1084 |
| 85 |  | 1085 |
| 86 |  | 1086 |
| 87 |  | 1087 |
| 88 |  | 1088 |
| 89 |  | 1089 |
| 90 |  | 1090 |
| 91 |  | 1091 |
| 92 |  | 1092 |
| 93 |  | 1093 |
| 94 |  | 1094 |
| 95 |  | 1095 |
| 96 |  | 1096 |
| 97 |  | 1097 |
| 98 |  | 1098 |
| 99 |  | 1099 |

## Variable DB type 14: ×┣Cmd Process List

| Field | Label | Observed storage code |
| --- | --- | --- |
| 0 | User ID | 1000 |
| 1 | User Agility | 1001 |
| 2 | Target ID | 1002 |
| 3 | Skill to Use | 1003 |

## Variable DB type 15: ×┗Reward List

| Field | Label | Observed storage code |
| --- | --- | --- |
| 0 | EXP Gain | 1000 |
| 1 | Money Gain | 1001 |
| 2 | EXP Multiplier \[Base 100\] | 1002 |
| 3 | Money Multiplier \[Base 100\] | 1003 |
| 4 |  | 1004 |
| 5 |  | 1005 |
| 6 |  | 1006 |
| 7 |  | 1007 |
| 8 |  | 1008 |
| 9 |  | 1009 |
| 10 |  | 1010 |
| 11 |  | 1011 |
| 12 |  | 1012 |
| 13 |  | 1013 |
| 14 |  | 1014 |
| 15 |  | 1015 |
| 16 |  | 1016 |
| 17 |  | 1017 |
| 18 |  | 1018 |
| 19 |  | 1019 |
| 20 | \[Item Drop Count\] | 1020 |
| 21 | Item Drop ID | 1021 |
| 22 | Item Drop ID | 1022 |
| 23 | Item Drop ID | 1023 |
| 24 | Item Drop ID | 1024 |
| 25 | Item Drop ID | 1025 |
| 26 | Rest Omitted | 1026 |
| 27 |  | 1027 |
| 28 |  | 1028 |
| 29 |  | 1029 |
| 30 |  | 1030 |
| 31 |  | 1031 |
| 32 |  | 1032 |
| 33 |  | 1033 |
| 34 |  | 1034 |
| 35 |  | 1035 |
| 36 |  | 1036 |
| 37 |  | 1037 |
| 38 |  | 1038 |
| 39 |  | 1039 |
| 40 |  | 1040 |
| 41 |  | 1041 |
| 42 |  | 1042 |
| 43 |  | 1043 |
| 44 |  | 1044 |
| 45 |  | 1045 |
| 46 |  | 1046 |
| 47 |  | 1047 |
| 48 |  | 1048 |
| 49 |  | 1049 |
| 50 |  | 1050 |
| 51 |  | 1051 |
| 52 |  | 1052 |
| 53 |  | 1053 |
| 54 |  | 1054 |
| 55 |  | 1055 |
| 56 |  | 1056 |
| 57 |  | 1057 |
| 58 |  | 1058 |
| 59 |  | 1059 |

## Variable DB type 16: ×Shop Temp Data

| Field | Label | Observed storage code |
| --- | --- | --- |
| 0 | Sell Item Name | 2000 |
| 1 | Sell Item ID | 1000 |
| 2 | Price | 1001 |
| 3 | Quantity | 1002 |
| 4 | (Equipment Quantity) | 1003 |
| 5 | Description | 2001 |
| 6 | (Purchasable \[0/1\]) | 1004 |
| 7 | (Member 1 Equippable) | 1005 |
| 8 | (Member 2 Equippable) | 1006 |
| 9 | (Member 3 Equippable) | 1007 |
| 10 | (Member 4 Equippable) | 1008 |
| 11 | (Member 5 Equippable) | 1009 |
| 12 | (Member 6 Equippable) | 1010 |
| 13 | (Equipment Status String) | 2002 |

## Variable DB type 17: ×Allies Temp Data

| Field | Label | Observed storage code |
| --- | --- | --- |
| 0 | \[Temp\] Post-Calc Max HP | 1000 |
| 1 | \[Temp\] Post-Calc Max SP | 1001 |
| 2 | \[Temp\] Post-Calc Attack | 1002 |
| 3 | \[Temp\] Post-Calc Defense | 1003 |
| 4 | \[Temp\] Post-Calc Magic Atk | 1004 |
| 5 | \[Temp\] Post-Calc Magic Def | 1005 |
| 6 | \[Temp\] Post-Calc Agility | 1006 |
| 7 | \[Temp\] Post-Calc Accuracy | 1007 |
| 8 | \[Temp\] Post-Calc Evasion | 1008 |
| 9 | \[Temp\]Post-Calc Critical Rate | 1009 |
| 10 | \[Temp\] Has States on Map? | 1010 |
| 11 | \[Temp\] HP Auto Change | 1011 |
| 12 | \[Temp\] SP Auto Change | 1012 |
| 13 | \[Tmp\] UntilNextStateRemove | 1013 |
| 14 | \[Tmp\] NextStateRemoveMax | 1014 |
| 15 | \[Temp\] State Names | 2000 |
| 16 | \[Temp\] Sealed? | 1015 |
| 17 | \[Store\] Menu Skill Position | 1016 |
| 18 | \[Store\] Battle Skill Position | 1017 |
| 19 | \[Store\] Battle Item Position | 1018 |
| 20 | \[Store\] Battle Command Pos | 1019 |

## Variable DB type 18: Base System Variables

| Field | Label | Observed storage code |
| --- | --- | --- |
| 0 | Number | 1000 |
| 1 | String | 2000 |

## Variable DB type 19: Universal Window Items

| Field | Label | Observed storage code |
| --- | --- | --- |
| 0 | Item Text | 2000 |
| 1 | Item ID | 1000 |
| 2 | Selectable? \[1:Yes\] | 1001 |
| 3 | Quantity Left/Point Cost | 1002 |
| 4 | Number Prefix | 2001 |
| 5 | Number Suffix | 2002 |
| 6 | Description | 2003 |
| 7 | \[Option\] Spare Number A | 1003 |
| 8 | \[Option\] Spare Number B | 1004 |
| 9 | \[Option\] Spare String A | 2004 |
| 10 | \[Option\] Spare String B | 2005 |

## System DB type 0: Map Settings

| Field | Label | Observed storage code |
| --- | --- | --- |
| 0 | Map Filename | 2000 |
| 1 | BGM Number (From List) | 1000 |
| 2 | BGS Number (From List) | 1001 |
| 3 | Loop: 1 Horz/2 Vert/3 Both | 1002 |
| 4 | Background Number | 1003 |
| 5 | BGM Filename (Number=-3) | 2001 |
| 6 | BGS Filename (Number=-3) | 2002 |
| 7 | BG Filename (Number=-3) | 2003 |

## System DB type 1: BGM List

| Field | Label | Observed storage code |
| --- | --- | --- |
| 0 | Filename | 2000 |
| 1 | Playback Volume \[%\] | 1000 |
| 2 | Playback Pitch \[%\] | 1001 |
| 3 | Loop Start (ms)/Key ± | 1002 |

## System DB type 2: BGS List

| Field | Label | Observed storage code |
| --- | --- | --- |
| 0 | Filename | 2000 |
| 1 | Playback Volume \[%\] | 1000 |
| 2 | Playback Pitch \[%\] | 1001 |
| 3 | Loop Start (ms) | 1002 |

## System DB type 3: SE List

| Field | Label | Observed storage code |
| --- | --- | --- |
| 0 | Filename | 2000 |
| 1 | Playback Volume \[%\] | 1000 |
| 2 | Playback Pitch \[%\] | 1001 |
| 3 | Memory Release Mode | 1002 |

## System DB type 4: String Variables

| Field | Label | Observed storage code |
| --- | --- | --- |

## System DB type 5: System Strings

| Field | Label | Observed storage code |
| --- | --- | --- |

## System DB type 6: System Variables

| Field | Label | Observed storage code |
| --- | --- | --- |

## System DB type 7: Position List

| Field | Label | Observed storage code |
| --- | --- | --- |
| 0 | Map ID | 1000 |
| 1 | X Position (on Map) | 1001 |
| 2 | Y Position (on Map) | 1002 |

## System DB type 8: Character Sprites

| Field | Label | Observed storage code |
| --- | --- | --- |
| 0 | Filename | 2000 |

## System DB type 9: Shadow Sprites

| Field | Label | Observed storage code |
| --- | --- | --- |
| 0 | Filename | 2000 |

## System DB type 10: Window Images

| Field | Label | Observed storage code |
| --- | --- | --- |
| 0 | Image Filename | 2000 |
| 1 | Vertical Divisions (V-Div Only) | 1000 |

## System DB type 11: Transition Types

| Field | Label | Observed storage code |
| --- | --- | --- |
| 0 | Filename (Monochrome) | 2000 |

## System DB type 12: Text Colors

| Field | Label | Observed storage code |
| --- | --- | --- |
| 0 | Red (0-255) | 1000 |
| 1 | Green (0-255) | 1001 |
| 2 | Blue (0-255) | 1002 |

## System DB type 13: Background/Fog

| Field | Label | Observed storage code |
| --- | --- | --- |
| 0 | Image Filename | 2000 |
| 1 | X Movement Speed | 1000 |
| 2 | Y Movement Speed | 1001 |
| 3 | Link Position to Map? | 1002 |

## System DB type 14: Normal Variables

| Field | Label | Observed storage code |
| --- | --- | --- |

## System DB type 15: Spare Variables 1

| Field | Label | Observed storage code |
| --- | --- | --- |

## System DB type 16: Spare Variables 2

| Field | Label | Observed storage code |
| --- | --- | --- |

## System DB type 17: Spare Variables 3

| Field | Label | Observed storage code |
| --- | --- | --- |

## System DB type 18: Spare Variables 4

| Field | Label | Observed storage code |
| --- | --- | --- |

## System DB type 19: Spare Variables 5

| Field | Label | Observed storage code |
| --- | --- | --- |

## System DB type 20: Spare Variables 6

| Field | Label | Observed storage code |
| --- | --- | --- |

## System DB type 21: Spare Variables 7

| Field | Label | Observed storage code |
| --- | --- | --- |

## System DB type 22: Spare Variables 8

| Field | Label | Observed storage code |
| --- | --- | --- |

## System DB type 23: Spare Variables 9

| Field | Label | Observed storage code |
| --- | --- | --- |

## System DB type 24: Portraits

| Field | Label | Observed storage code |
| --- | --- | --- |
| 0 | Portrait Filename | 2000 |

## System DB type 25: 

| Field | Label | Observed storage code |
| --- | --- | --- |
| 0 |  | 2000 |

## System DB type 26: 

| Field | Label | Observed storage code |
| --- | --- | --- |
| 0 |  | 2000 |

## System DB type 27: 

| Field | Label | Observed storage code |
| --- | --- | --- |
| 0 |  | 2000 |

