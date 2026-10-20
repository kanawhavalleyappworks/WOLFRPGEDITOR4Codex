# Basic System sample index: 3.691

English labels from the inspected 3.691 translation package: translation by Yumu, edited by Anya and Lolo; sample-data translation by Yumu. Original engine/Basic System by SmokingWOLF. See [sources and credits](sources.md). Reviewed 2026-10-20. This is an installation snapshot, not an engine-version-independent ID registry.

Observed sample: 225 common-event slots. Names/argument labels are lookup aids. They are not permission to overwrite occupied slots. Public-looking wrappers and internal `X` routines must be distinguished by inspecting their bodies and callers. Base System 3 in this sample is distinct from the engine version 3.691.

## Common events

| ID | Name | Numeric inputs | String inputs | Return label | Purpose / source memo |
| --- | --- | --- | --- | --- | --- |
| 0 | ○ Change Items | Item ID; Amount \[±\]; Show Message? (3) |  (0) |  | Adds or removes items. To remove, use a negative amount. |
| 1 | ○ Change Weapons | Weapon ID; Amount \[±\]; Show Message? (3) |  (0) |  | Adds or removes weapons. To remove, use a negative amount. |
| 2 | ○ Change Armors | Armor ID; Amount \[±\]; Show Message? (3) |  (0) |  | Adds or removes armors. To remove, use a negative amount. |
| 3 | ○ Change Money | Money Amount; Show Message? (2) |  (0) |  | Increases or decreases the current amount of money. To decrease, use a negative amount. |
| 4 | ○ Recover or Damage | Type; Who?; Amount (3) |  (0) |  | Recovers or reduces HP/SP, or clears states. Full Recovery recovers all. Can be used on map or in battle. |
| 5 | ○ Change Members | Type; Who? (2) |  (0) |  | Adds or removes a member. No effect when there isn't any room in the party. Also works in battle. |
| 6 | ○ Change Ally Data | Target Ally; Which Data? (2) | New String (1) |  | Changes the ally's name, title, character sprite, or portrait. Also works in battle. |
| 7 | ○ Change Stats | Target Ally; Which Stat?; Amount; Show Message? (4) |  (0) |  | Increases or decreases a stat. Stats and growth rates can't go below 0. Use negative amount to decrease. Also works in battle. |
| 8 | ○ Change Skills | Target Ally; Which Skill?; Action (3) |  (0) |  | Adds or removes a skill. Also works in battle. |
| 9 | ○ Change States | Target Ally; State; Action (3) |  (0) |  | Adds or removes a state. Also works in battle. |
| 10 | ○ Change EXP/Level | Target Ally; Action; Amount; Show Message? (4) |  (0) |  | Increases or decreases EXP or level. Decreasing EXP doesn't lower level. Also works in battle. |
| 11 | ○ Change Weapon Equipment | Target Ally; Equipment Slot; Weapon ID (3) |  (0) | Supplied? | Changes equipment. If there's nothing for specified equipment, one is auto-supplied, and "1" is returned. Also works in battle. |
| 12 | ○ Change Armor Equipment | Target Ally; Equipment Slot; Armor ID (3) |  (0) | Supplied? | Changes equipment. If there's nothing for specified equipment, one is auto-supplied, and "1" is returned. Also works in battle. |
| 13 | ○ Change Battle Commands | Target Ally; Which Cmd?; Change To (3) |  (0) | Change Made? | Changes battle commands. Also works in battle. |
| 14 | ○ Open Menus | Which Menu? (1) |  (0) |  | Opens the save menu, items menu, etc. Only works on map. |
| 15 | ○ Change Save Availability | Mode (1) |  (0) |  | Allows or disallows saving. |
| 16 | --------------------------------- |  (0) |  (0) |  |  |
| 17 | ▲Get Item Quantity | Item (1) |  (0) | Item Quantity | Returns the quantity of the specified item. |
| 18 | ▲Get Weapon Quantity | Weapon (1) |  (0) | Weapon Quantity | Returns the quantity of the specified weapon. |
| 19 | ▲Get Armor Quantity | Armor (1) |  (0) | Armor Quantity | Returns the quantity of the specified armor. |
| 20 | ▲Get Current Money |  (0) |  (0) | Money | Returns the current amount of money. |
| 21 | ▲Get Equipment | Target Ally; Which Slot?; Equipment Type (3) |  (0) | Equipment ID | Returns equipment ID (0+), or -1 if none or if the specified equipment type (weapon/armor) differs. |
| 22 | ▲Get Ally Data \[Number\] | Target Ally; Data (2) |  (0) | Data Value | Returns the ally's numerical data. |
| 23 | ▲Get Ally Data \[String\] | Target Ally; Data (2) |  (0) | Data String | Returns the ally's string data. |
| 24 | ▲Check for State | Target Ally; State (2) |  (0) | Yes: 1/No: 0 | Check whether an ally has a state. If they do, "1" is returned. |
| 25 | ▲Check for Skill | Target Ally; Skill (2) |  (0) | Learned? (Yes: 1) | Check whether an ally has learned a skill. If they have, 1 is returned, otherwise 0. |
| 26 | ▲Check for Battle Command | Target Ally; Which Position?; Command (3) |  (0) | Exists? (Yes: 1+) | Returns the position of the ally's battle command (1-8), or 0 if not there. (Commands added by equipment are ignored.) |
| 27 | --------------------------------- |  (0) |  (0) |  |  |
| 28 | ◆Start Battle | Enemy Group ID; Can Flee; On Defeat; Battle BGM (4) |  (0) | Win1/Lose-1/Flee0 | Starts a battle. The result of the battle is returned. (1: Victory, -1: Defeat, 0: Flee) |
| 29 | ◆\[Battle\] Add Enemy | Position; Enemy; Overwrite Option (3) |  (0) |  | Only in battle: adds an enemy (or replaces one) in the specified spot (1-7). |
| 30 | ◆\[Battle\] Show Message | Mode (1) | Message (1) |  | Only in battle: shows a message in the middle of the screen. |
| 31 | ◆\[Battle\] Apply Damage | Target; Amount (2) |  (0) |  | Only in battle: shows a damage popup and reduces HP. |
| 32 | --------------------------------- |  (0) |  (0) |  |  |
| 33 | \[1\] Shop: Initialize |  (0) |  (0) |  | Resets merchandise. Use this at the beginning of the shop process. Then call "\[2\] Shop: Add Merchandise". |
| 34 | \[2\] Shop: Add Merchandise | What to Add?; Item \[A\]; Weapon \[B\]; Armor \[C\] (4) |  (0) |  | Adds an item/weapon/armor to sell in the shop. Once done adding, call "\[3\] Shop: Open". |
| 35 | \[3\] Shop: Open | Shop Type (1) |  (0) |  | Starts up the shop. If no merchandise is set, you can only sell. |
| 36 | --------------------------------- |  (0) |  (0) |  |  |
| 37 | ◇Random Encounter | Steps to Appear; Enemy Group 1; Enemy Group 2; Enemy Group 3 (4) |  (0) | Enemy Appeared? | Increments the counter when called. When it reaches a set value, one of three enemy groups appears at random. |
| 38 | --------------------------------- |  (0) |  (0) |  |  |
| 39 | ■Switch Pixel Movement | Mode (1) |  (0) |  | Use by turning on and off. CAUTION: A few pixels of misalignment at the start of an event can prevent movement during it. |
| 40 | --------------------------------- |  (0) |  (0) |  |  |
| 41 | --------------------------------- |  (0) |  (0) |  |  |
| 42 | --------------------------------- |  (0) |  (0) |  |  |
| 43 | --------------------------------- |  (0) |  (0) |  |  |
| 44 | ■■■■■■■■■■■■■■■■■■ |  (0) |  (0) |  |  |
| 45 | ■Don't Edit/Call Events Below■ |  (0) |  (0) |  |  |
| 46 | ■■■■----------------- ■■■■ |  (0) |  (0) |  |  |
| 47 | ■■\[Common: Internal Processing\]■■ |  (0) |  (0) |  |  |
| 48 | X\[Com\]Base System Auto-Init |  (0) |  (0) |  |  |
| 49 | X\[Com\]Play System Sound | Sound to Play (1) |  (0) |  |  |
| 50 | X\[Com\]Change Items | Item ID; Amount (2) |  (0) | Actual Change |  |
| 51 | X\[Com\]Change Weapons | Weapon ID; Amount (2) |  (0) | Actual Change |  |
| 52 | X\[Com\]Change Armors | Armor ID; Amount (2) |  (0) | Actual Change |  |
| 53 | X\[Com\]Change Money | Amount (1) |  (0) |  |  |
| 54 | X\[Com\]Get Item Quantity | Item ID (1) |  (0) | Quantity |  |
| 55 | X\[Com\]Get Weapon Quantity | Weapon ID (1) |  (0) | Quantity |  |
| 56 | X\[Com\]Get Armor Quantity | Armor ID (1) |  (0) | Quantity |  |
| 57 | X\[Com\]Get Current Money |  (0) |  (0) | Money |  |
| 58 | X\[Com\]Add/Remove Skill | Ally ID; Skill ID; Learn? Forget? (3) |  (0) |  |  |
| 59 | X\[Com\]Wait(PressKeyToEnd) | Wait Frames; Minimum Wait (2) |  (0) |  |  |
| 60 | X\[Com\]Wait 2(PressKeyToSpdUp) | Wait Frames (1) |  (0) |  |  |
| 61 | X\[Com\]Calc Spd-Up Wait Frames | Wait Frames (1) |  (0) | Actual Wait |  |
| 62 | ■■\[Common: Screen Processing\]■■ |  (0) |  (0) |  |  |
| 63 | X\[Com\]Message Window |  (0) |  (0) |  |  |
| 64 | X\[Com\]Draw Universal Window | Mode; Cursor Position; \[Disp\] Description; \[Disp\] Animation (4) |  (0) |  | Draws what's stored in the database. Description is used only in "Display" mode. |
| 65 | X\[Com\]U-Window: Select | Mode; Option (2) |  (0) | Selected ID | *Canceled: Returns -100 *Ended with Sub/Left/Right Key: Returns -300 *One Key Press Mode: If selecting, returns -200 |
| 66 | X\[Com\]U-Window: Update Desc |  (0) | Description Text (1) |  |  |
| 67 | X\[Com\]Execute Full Effect | Mode; Frames (2) |  (0) |  |  |
| 68 | ■■■■■■■■■■■■■■■■■■■ |  (0) |  (0) |  |  |
| 69 | ■■\[Map: Internal Processing\]■■ |  (0) |  (0) |  |  |
| 70 | X\[Map\]Change Parameter | Ally ID; Target Parameter; Amount; Show Message? (4) |  (0) |  | Increase or decrease a parameter value. After that, temporary values must be updated in "Recalculate Temp Values" mode. |
| 71 | X\[Map\]Get Parameter | Ally ID; Target Parameter (2) |  (0) | Parameter Value |  |
| 72 | X\[Map\]Change Parameter (String) | Ally ID; Target Parameter (2) | String to Set (1) |  | Changes an ally's string parameter value. |
| 73 | X\[Map\]Get Parameter (String) | Ally ID; Target Parameter (2) |  (0) | Returned String | Gets an ally's string parameter value. |
| 74 | X\[Map\]Level Up/Down | Ally ID; Level Amount; Option (3) |  (0) | Actual Change |  |
| 75 | X\[Map\]Add/Remove State | Ally ID; State; Action (3) |  (0) |  |  |
| 76 | X\[Map\]Update States |  (0) |  (0) |  |  |
| 77 | X\[Map\]Change Battle Commands | Ally ID; Command Slot; Command ID (3) |  (0) | Change Made? |  |
| 78 | X\[Map\]Get Battle Command | Ally ID; Command Slot (2) |  (0) | Command ID |  |
| 79 | X\[Map\]Update Party Info |  (0) |  (0) |  |  |
| 80 | X\[Map\]Update Party Sprites |  (0) |  (0) |  |  |
| 81 | ■■\[Shop-Related Processing\]■■ |  (0) |  (0) |  |  |
| 82 | X\[Map\]Initialize Shop Items |  (0) |  (0) |  |  |
| 83 | X\[Map\]Add Shop Item | 商品コード (1) |  (0) |  |  |
| 84 | X\[Map\]Open Shop | お店のタイプ (1) |  (0) |  |  |
| 85 | X\[Map\]┣ Draw Shop | 処理モード; \[2\]カーソル位置; 商品選択位置 (3) |  (0) |  |  |
| 86 | X\[Map\]┗ Update Shop Internal Data | 買う？売る？ (1) |  (0) |  |  |
| 87 | ■■\[Menu Screen Processing\]■■ |  (0) |  (0) |  |  |
| 88 | X\[Map\]Draw Menu | 処理モード; カーソル位置 (2) |  (0) |  |  |
| 89 | X┗\[Map\]Update Menu Variables |  (0) |  (0) |  |  |
| 90 | X\[Map\]Draw Character Box | 処理モード; 表示位置; 表示主人公ID (3) |  (0) |  |  |
| 91 | X\[Map\]Character Box: Calc Pos | 表示位置\[0-..\] (1) |  (0) |  |  |
| 92 | X\[Map\]Character Box: Draw All | 処理モード (1) |  (0) |  |  |
| 93 | X\[Map\]Draw Equip Screen | 処理モード; \[1\]主人公ID; \[2\]カーソル位置 (3) |  (0) |  |  |
| 94 | X\[Map\]Draw Save/Load Screen | 処理モード; カーソル位置; ページ位置 (3) |  (0) |  |  |
| 95 | X\[Map\]Draw System Screen | 処理モード; カーソル位置 (2) |  (0) |  |  |
| 96 | X\[Map\]Display Dmg/Recovery Popup | 表示位置X; 表示位置Y; 数値/状態番号; 表示タイプ (4) |  (0) |  |  |
| 97 | X\[Map\]Display Char HP/SP Recovery | キャラ位置\[0-5\]; HP回復量; SP回復量 (3) |  (0) |  |  |
| 98 | X\[Map\]Display Character State | キャラ位置\[0-5\]; 状態番号 (2) |  (0) |  |  |
| 99 | X\[Map\]Display Remaining Item Count | 表示モード; アイテムコード (2) |  (0) |  |  |
| 100 | X\[Map\]Display Mini Window | 表示モード (1) | １行目表示文; ２行目表示文; ３行目表示文 (3) |  |  |
| 101 | X\[Map\]Display Menu Message | 処理モード (1) | 表示文 (1) |  |  |
| 102 | X\[Map\]Draw Upper Status | 処理モード; \[1\]主人公ID (2) |  (0) |  |  |
| 103 | ■■\[Menu Internal Processing\]■■ |  (0) |  (0) |  |  |
| 104 | X\[Map\]Set Ally ID | ﾊﾟｰﾃｨ位置\[0-\]; 設定主人公ID (2) |  (0) |  | 前からX番目(0番から開始)にいる主人公のIDを設定します |
| 105 | X\[Map\]Get Ally ID | ﾊﾟｰﾃｨ位置\[0-\] (1) |  (0) | 主人公ID | 前からX番目(0番から開始)にいる主人公のIDを取得します。なければ-1を返します |
| 106 | X\[Map\]Get Equipment ID | 主人公ID; 装備箇所 (2) |  (0) | 装備コード |  |
| 107 | X\[Map\]Set Equipment ID | 主人公ID; 装備箇所; 装備コード (3) |  (0) |  |  |
| 108 | X\[Map\]Select Character Box | 初期選択位置; オプション (2) |  (0) | 選択ｷｬﾗ\[0-5\] |  |
| 109 | X\[Map\]Select Equipment Box | 主人公位置; キャラ切替可 (2) |  (0) | 主人公ID |  |
| 110 | X\[Map\]Create Item List |  (0) |  (0) |  |  |
| 111 | X\[Map\]Create Skill List | 対象主人公ID (1) |  (0) |  |  |
| 112 | X\[Map\]Create Equipment List | 対象主人公; 表示する装備 (2) |  (0) |  |  |
| 113 | X\[Map\]Change Equipment | 対象主人公ID; 装備箇所; 装備コード (3) |  (0) | 不足分補充 | 武器・防具の装着・解除処理を行います。装備時、足りなければ「不足分補充」に1を返します。 |
| 114 | X\[Map\]Calc Equip Stat Changes | 外す装備ｺｰﾄﾞ; 装着装備ｺｰﾄﾞ; 結果を加算？ (3) |  (0) | 装備外せない |  |
| 115 | X\[Map\]Set Key Repeat | 設定値\[0-4\] (1) |  (0) |  |  |
| 116 | X\[Map\]Get Cursor Memory Pos | 取得モード; 主人公ID (2) |  (0) | キー位置 |  |
| 117 | X\[Map\]Set Cursor Memory Pos | 取得モード; 主人公ID; ｶｰｿﾙ位置 (3) |  (0) |  |  |
| 118 | X\[Map\]Use Item | 使用ｱｲﾃﾑｺｰﾄﾞ (1) |  (0) |  |  |
| 119 | X\[Map\]Use Skill | 技能コード; 発動者ID; アイテム経由? (3) |  (0) | 使用した？ |  |
| 120 | X\[Map\]Item Use: Consume | アイテムコード (1) |  (0) | 次使用可能? |  |
| 121 | X\[Map\]Skill Use: Consume | 発動主人公ID; 使用技能 (2) |  (0) | 次使用可能? |  |
| 122 | X\[Map\]CalcTempStats &lt;Initialize&gt; | 対象主人公ID (1) |  (0) |  |  |
| 123 | X\[Map\]CalcTempStats &lt;Equipments&gt; | 対象主人公ID (1) |  (0) |  |  |
| 124 | X\[Map\]CalcTempStats &lt;StatusEffects&gt; | 対象主人公ID (1) |  (0) |  |  |
| 125 | ■■\[Menu Execution Processing\]■■ |  (0) |  (0) |  |  |
| 126 | X\[Map\]ParallelProcessWhenWalking |  (0) |  (0) |  |  |
| 127 | X\[Map\]Start Menu |  (0) |  (0) |  |  |
| 128 | X┣\[Map\]Execute Items Menu | 処理モード (1) |  (0) |  |  |
| 129 | X┣\[Map\]Execute Skills Menu | 処理モード (1) |  (0) |  |  |
| 130 | X┣\[Map\]Execute Equip Menu | 処理モード (1) |  (0) |  |  |
| 131 | X┣\[Map\]Execute Save Menu | セーブ? ロード?; モード (2) |  (0) | セーブ箇所 | セーブ時は、「セーブ箇所」を返します。セーブしていなければ-1を返します |
| 132 | X┗\[Map\]Execute System Menu |  (0) |  (0) |  |  |
| 133 | ■■■■■■■■■■■■■■■■■■■ |  (0) |  (0) |  |  |
| 134 | ■■\[Battle: Internal Processing\]■■ |  (0) |  (0) |  |  |
| 135 | X\[Bat\]Change Parameter | 対象戦闘ｽﾛｯﾄ; 対象パラメータ; 増減値 (3) |  (0) | 戦闘不能？ |  |
| 136 | X\[Bat\]Get Parameter | 対象戦闘ｽﾛｯﾄ; 対象パラメータ (2) |  (0) | パラメータ値 |  |
| 137 | X\[Bat\]Add/Remove State | 戦闘ｽﾛｯﾄ; 付与する状態; 付与？消去？; メッセージ有無 (4) |  (0) |  |  |
| 138 | X\[Bat\]┗ Display State Message | 対象スロット; 状態番号; 付与？消去？ (3) |  (0) |  |  |
| 139 | X\[Bat\]Update States | 対象スロット; 処理タイミング; ┗\[3\]攻･精ON? (3) |  (0) |  |  |
| 140 | X\[Bat\]Initialize Battle Variables |  (0) |  (0) |  |  |
| 141 | X\[Bat\]Get Ally ID in Slot | 対象戦闘ｽﾛｯﾄ (1) |  (0) | 主人公ID |  |
| 142 | X\[Bat\]Update Ally | 主人公ID (1) |  (0) | 処理された？ | 戦闘中かつ指定した主人公IDのｷｬﾗが参戦している場合だけ、そのキャラのパラメータ更新＋描画更新を行います。 |
| 143 | X\[Bat\]Copy Allies DB to Battle DB | 入力先戦闘DB; 読込主人公ID; オプション (3) |  (0) |  |  |
| 144 | X\[Bat\]Copy Enemies DB to Battle DB | 入力先戦闘DB; 読込敵ID; オプション (3) |  (0) |  |  |
| 145 | X\[Bat\]Get Equipment ID | 対象戦闘ｽﾛｯﾄ; 装備箇所 (2) |  (0) | 装備コード |  |
| 146 | X\[Bat\]CalcTempStats &lt;Initialize&gt; | 対象戦闘ｽﾛｯﾄ (1) |  (0) |  |  |
| 147 | X\[Bat\]CalcTempStats &lt;Equipments&gt; | 対象戦闘ｽﾛｯﾄ; 使用する武器 (2) |  (0) | 武器ある？ |  |
| 148 | X\[Bat\]CalcTempStats &lt;StatusEffects&gt; | 対象戦闘ｽﾛｯﾄ; オプション (2) |  (0) |  |  |
| 149 | X\[Bat\]Return Battle DB to Allies DB | 入力元戦闘DB; 格納主人公ID (2) |  (0) |  |  |
| 150 | X\[Bat\]Get Battle Command | 対象戦闘ｽﾛｯﾄ; コマンド位置 (2) |  (0) | コマンド番号 |  |
| 151 | X\[Bat\]Set Battle Command | 対象戦闘ｽﾛｯﾄ; コマンド位置; 設定コマンド; オプション (4) |  (0) | セット成功？ |  |
| 152 | X\[Bat\]Create Battle Cmd List | 対象戦闘ｽﾛｯﾄ (1) |  (0) |  |  |
| 153 | X\[Bat\]Create Item List |  (0) |  (0) |  |  |
| 154 | X\[Bat\]Create Skill List | 対象戦闘ｽﾛｯﾄ (1) |  (0) |  | 戦闘時に使用可能な技能一覧を計算して万能ウィンドウリストに格納します。指定するのは戦闘ｽﾛｯﾄです。 |
| 155 | X\[Bat\]Get Cursor Memory Pos | 取得モード; 対象戦闘ｽﾛｯﾄ (2) |  (0) | キー位置 |  |
| 156 | X\[Bat\]Set Cursor Memory Pos | 取得モード; 対象戦闘ｽﾛｯﾄ; ｶｰｿﾙ位置 (3) |  (0) |  |  |
| 157 | X\[Bat\]Register Command | 発動戦闘ｽﾛｯﾄ; 発動技能; ｵﾌﾟｼｮﾝ; \[AI\]使用対象 (4) |  (0) | 即100/対象0- | 対象選択をキャンセルしたら-1 |
| 158 | X\[Bat\]Select Item | 発動者スロット (1) |  (0) | 使用対象 |  |
| 159 | X\[Bat\]Select Skill | 発動スロット; \[A\]発動技能; モード (3) |  (0) | 使用対象 |  |
| 160 | X\[Bat\]Process AI Actions | 対象戦闘ｽﾛｯﾄ (1) |  (0) |  |  |
| 161 | X\[Bat\]Select Ally Target | 初期選択位置; オプション (2) |  (0) | 選択ｷｬﾗ\[0-5\] |  |
| 162 | X\[Bat\]Select Enemy Target |  (1) |  (0) | 選択対象 |  |
| 163 | X\[Bat\]Get Enemy/Ally Target | 対象ｱｸｼｮﾝ; どこまで処理済 (2) |  (0) | 単体対象 | 結果：　次の対象がいなくなれば-1を返します。 |
| 164 | X\[Bat\]Execute Command | 処理番号; 武器の指定; ｶｳﾝﾀｰ抑制? (3) |  (0) |  |  |
| 165 | X\[Bat\]┗ Execute Skill on One | 発動スロット; 発動技能; 対象ｽﾛｯﾄ(単); オプション (4) |  (0) |  |  |
| 166 | X\[Bat\]    ┗ Check Counter | 対象ｽﾛｯﾄ; 技能番号; 発動者スロット (3) |  (0) | ｶｳﾝﾀｰ\[状態\] |  |
| 167 | X\[Bat\]Execute Counter | 処理番号; 武器の指定 (2) |  (0) |  |  |
| 168 | X\[Bat\]Attempt Transform | 対象ｽﾛｯﾄ; タイミング (2) |  (0) |  |  |
| 169 | X\[Bat\]Item Use: Consume | アイテムコード (1) |  (0) |  |  |
| 170 | X\[Bat\]Skill Use: Consume | 対象戦闘ｽﾛｯﾄ; 使用技能 (2) |  (0) |  |  |
| 171 | X\[Bat\]Defeat Enemy | 対象戦闘ｽﾛｯﾄ; モード (2) |  (0) |  |  |
| 172 | X\[Bat\]Check Win/Lose | 判定モード (1) |  (0) | 勝敗 1/0/-1 | 味方の勝利なら1、敗北なら-1を返す。 |
| 173 | X\[Bat\]┗ Display Remaining Turns | 残りターン数 (1) |  (0) |  | ターンの変わり際に残りターン数を表示する |
| 174 | X\[Bat\]Ally Box: Calc Position | 表示位置\[0-..\] (1) |  (0) |  |  |
| 175 | X\[Bat\]Enemy: Calc Position | 表示位置\[0-..\] (1) |  (0) |  |  |
| 176 | X\[Bat\]Get Basic State | 対象戦闘ｽﾛｯﾄ; 取得する状態 (2) |  (0) | 状態はON？ |  |
| 177 | ■■\[Battle: Screen Processing\]■■ |  (0) |  (0) |  |  |
| 178 | X\[Bat\]Ally Box: Draw One | モード; 表示位置; 戦闘スロット (3) |  (0) |  |  |
| 179 | X\[Bat\]Enemy: Draw One | モード; 対象戦闘ｽﾛｯﾄ (2) |  (0) |  |  |
| 180 | X\[Bat\]Draw Background | モード (1) |  (0) |  |  |
| 181 | X\[Bat\]Display Dmg/Recovery Popup | 表示位置X; 表示位置Y; 数値/状態番号; 表示タイプ (4) |  (0) |  |  |
| 182 | X\[Bat\]Display Battle Message | モード (1) | 表示文 (1) |  |  |
| 183 | X\[Bat\]Draw Skill Effect | アニメ番号; 対象X座標; 対象Y座標; 対象スロット (4) |  (0) | 全体用？ |  |
| 184 | X\[Bat\]Display Warning Message | 処理モード (1) | 表示文 (1) |  |  |
| 185 | X\[Bat\]Draw Upper Status | 処理モード; \[1\]戦闘ｽﾛｯﾄ (2) |  (0) |  |  |
| 186 | X\[Bat\]Draw Rewards Screen | 処理モード (1) |  (0) | 続行有り？ |  |
| 187 | ■■\[Battle: Execution Processing\]■■ |  (0) |  (0) |  |  |
| 188 | X◆Battle Process | 敵グループ番号; 逃走可能？; 敗北時の処理; 戦闘BGM (4) |  (0) | 勝1/負-1/逃0 |  |
| 189 | X┣◆Initialize Battle |  (0) |  (0) |  |  |
| 190 | X┣◆Place Battle Character | エフェクト有り？ (1) |  (0) |  |  |
| 191 | X┣◆Set Action | コマンドモード; 逃走可能フラグ (2) |  (0) | 逃走？ |  |
| 192 | X┃┣◆Select Ally Command | 対象戦闘ｽﾛｯﾄ; オプション処理 (2) |  (0) | 結果\[0/1/-1\] | 選択の返り値は、　0＝何か選択した　1＝選択不能　2=AI処理　-1=ｷｬﾝｾﾙした　-2=無進行ｺﾏﾝﾄﾞ選択 10=戦終了 |
| 193 | X┃┗◆Process Enemy/Ally AI | モード (1) |  (0) |  |  |
| 194 | X┣◆Calculate Action Order |  (0) |  (0) |  |  |
| 195 | X┣◆Execute 1-Turn Process |  (0) |  (0) |  |  |
| 196 | X┃┣◆Check If Can Act | 行動ﾘｽﾄ番号 (1) |  (0) | 行動可能？ |  |
| 197 | X┃┗◆1-Action Loop | 行動ﾘｽﾄ番号; カウンター処理? (2) |  (0) | 勝敗決定？ |  |
| 198 | X┣◆Turn End Process |  (0) |  (0) | 戦闘終了？ |  |
| 199 | X┣◆Update Allies DB |  (0) |  (0) |  |  |
| 200 | X┣◆Rewards Getting Process | 勝敗フラグ (1) |  (0) |  |  |
| 201 | X┗◆Battle End Process |  (0) |  (0) |  |  |
| 202 | ■■■■■■■■■■■■■■■■■■■ |  (0) |  (0) |  |  |
| 203 | ○\[Editable\] At Battle Start |  (0) |  (0) |  |  |
| 204 | ○\[Editable\] At Turn Start |  (0) |  (0) |  |  |
| 205 | ○\[Editable\] At Turn End |  (0) |  (0) |  |  |
| 206 | ○\[Editable\] At Battle End |  (0) |  (0) |  |  |
| 207 | ■■■■■■■■■■■■■■■■■■■ |  (0) |  (0) |  |  |
| 208 | \[Base System Ver. 3.35 Manual\] |  (0) |  (0) |  |  |
| 209 | ■■■■■■■■■■■■■■■■■■■ |  (0) |  (0) |  |  |
| 210 | ■Events Below Are Free to Use■ |  (0) |  (0) |  |  |
| 211 | ■■■■■■■■■■■■■■■■■■■ |  (0) |  (0) |  |  |
| 212 | Talk Command |  (0) |  (0) |  | This is just here as an example, so you're free to delete it. |
| 213 | Game Over Event |  (0) |  (0) |  |  |
| 214 | WOLF RPG Editor Event |  (0) |  (0) |  | The event called when the WOLF RPG Editor item is used. |

## Database types

| Database | Type | Name | Fields | Entries |
| --- | --- | --- | --- | --- |
| User DB | 0 | Skills | 37 | 44 |
| User DB | 1 | ┗ Animations | 15 | 34 |
| User DB | 2 | Items | 21 | 25 |
| User DB | 3 | Weapons | 30 | 24 |
| User DB | 4 | Armors | 38 | 37 |
| User DB | 5 | ┗ Equipment Types | 1 | 25 |
| User DB | 6 | Battle Commands | 4 | 19 |
| User DB | 7 | Element Names | 1 | 10 |
| User DB | 8 | States | 46 | 24 |
| User DB | 9 | Enemies | 26 | 42 |
| User DB | 10 | ┣ Enemy Action AI | 48 | 40 |
| User DB | 11 | ┣ Element Resistances | 100 | 42 |
| User DB | 12 | ┗ State Resistances | 100 | 40 |
| User DB | 13 | Enemy Groups | 12 | 41 |
| User DB | 14 | ------------------------ | 0 | 1 |
| User DB | 15 | Terms | 32 | 1 |
| User DB | 16 | Images/Sounds | 21 | 1 |
| User DB | 17 | System Settings | 35 | 1 |
| Variable DB | 0 | Allies | 59 | 17 |
| Variable DB | 1 | ┣ Skill Learning Lv | 100 | 16 |
| Variable DB | 2 | ┣ Ally Action AI | 48 | 22 |
| Variable DB | 3 | ┣ Element Resistances | 100 | 40 |
| Variable DB | 4 | ┣ State Resistances | 100 | 16 |
| Variable DB | 5 | ┗ State List | 100 | 16 |
| Variable DB | 6 | Party | 7 | 1 |
| Variable DB | 7 | ┣ Owned Items | 1 | 10 |
| Variable DB | 8 | ┣ Owned Weapons | 1 | 10 |
| Variable DB | 9 | ┗ Owned Armors | 1 | 1 |
| Variable DB | 10 | ×┏Battle Temp Status | 78 | 18 |
| Variable DB | 11 | ×┣Element Resist Calc | 100 | 11 |
| Variable DB | 12 | ×┣State Resist Calc | 100 | 11 |
| Variable DB | 13 | ×┣State List | 100 | 11 |
| Variable DB | 14 | ×┣Cmd Process List | 4 | 100 |
| Variable DB | 15 | ×┗Reward List | 60 | 1 |
| Variable DB | 16 | ×Shop Temp Data | 14 | 15 |
| Variable DB | 17 | ×Allies Temp Data | 21 | 8 |
| Variable DB | 18 | Base System Variables | 2 | 100 |
| Variable DB | 19 | Universal Window Items | 11 | 200 |
| System DB | 0 | Map Settings | 8 | 4 |
| System DB | 1 | BGM List | 4 | 16 |
| System DB | 2 | BGS List | 4 | 6 |
| System DB | 3 | SE List | 4 | 20 |
| System DB | 4 | String Variables | 0 | 10 |
| System DB | 5 | System Strings | 0 | 90 |
| System DB | 6 | System Variables | 0 | 170 |
| System DB | 7 | Position List | 3 | 10 |
| System DB | 8 | Character Sprites | 1 | 10 |
| System DB | 9 | Shadow Sprites | 1 | 4 |
| System DB | 10 | Window Images | 2 | 3 |
| System DB | 11 | Transition Types | 1 | 10 |
| System DB | 12 | Text Colors | 3 | 30 |
| System DB | 13 | Background/Fog | 4 | 3 |
| System DB | 14 | Normal Variables | 0 | 18 |
| System DB | 15 | Spare Variables 1 | 0 | 4 |
| System DB | 16 | Spare Variables 2 | 0 | 5 |
| System DB | 17 | Spare Variables 3 | 0 | 4 |
| System DB | 18 | Spare Variables 4 | 0 | 1 |
| System DB | 19 | Spare Variables 5 | 0 | 1 |
| System DB | 20 | Spare Variables 6 | 0 | 1 |
| System DB | 21 | Spare Variables 7 | 0 | 1 |
| System DB | 22 | Spare Variables 8 | 0 | 1 |
| System DB | 23 | Spare Variables 9 | 0 | 10 |
| System DB | 24 | Portraits | 1 | 12 |
| System DB | 25 |  | 1 | 1 |
| System DB | 26 |  | 1 | 1 |
| System DB | 27 |  | 1 | 1 |

For field addresses, read the [database field locator](sample-database-schema-3.691.md). Runtime behavior still requires the relevant common-event body and a playtest.
