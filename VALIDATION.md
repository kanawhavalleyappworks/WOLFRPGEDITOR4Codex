# Validation record

Build date: 2026-10-20. This record describes checks actually performed, not requirements assumed to have passed.

## Skill and portability

- The skill-creator validator accepted the name, frontmatter, and absence of unfinished scaffold placeholders.
- Python helpers parsed and ran using Python 3.10 with standard-library imports only.
- The package was relocated to a different folder; local Markdown references resolved without the research folder or network.
- Offline searches located a system capability label and sample common-event interface.
- Synthetic project scans preserved input bytes and handled paths containing spaces and Japanese characters.
- Comparison detected same-size modifications, additions, and deletions; reported allowed changes visibly; ignored timestamp-only changes; accepted UTF-8/BOM and PowerShell-style UTF-16 JSON reports.
- Invalid/unhashed reports and parent-directory layout escapes were rejected.
- A Windows directory-junction fixture was skipped without traversing its target. This check required the unrestricted local test process because the restricted environment could not create a junction. The helper itself performs no elevated operation.
- A fresh ZIP extraction was compared byte-for-byte with the source payload and project-local copy.

## Actual WOLF 3.691 checks

The user's source installation was inventoried before testing: 677 files, 57,435,785 bytes, with four `.mps` maps. Editor.exe and Game.exe both reported file version `3.691.2026.408`. All engine execution occurred in a disposable project copy.

1. Native ALL text export emitted six basic-data files and four maps.
2. No-edit ALL import exited successfully.
3. A second ALL export matched all ten original exported text files byte-for-byte.
4. The copied settings export's `GAME_TITLE_MAIN` value was changed once, and BASIC import was run.
5. ALL re-export differed in exactly one file and only by the intended title string. The copied runtime `Game.dat` changed accordingly; other original project data remained byte-identical in the inspected comparison.
6. A final hash comparison of the user's original installation reported zero file changes.

The title probe checks native reconstruction/readback. It does not establish visual display of the title or a complete gameplay test.

## Reusable helper checks

From the extracted skill folder:

```text
python -B -m unittest discover -s tests -v
```

These tests use synthetic opaque files and never launch their dummy executable. The Windows junction check and native engine probes were build-time checks and are not automatically recreated by this command.

## Untested or incomplete areas

- Gameplay, GUI interaction, save/load behavior, graphical/audio presentation, and distribution launch.
- Clipboard event-code paste and Common Event file import in the real editor UI.
- Pro-only operations and versions other than the tested 3.691 profile.
- Every command parameter, hidden string operation, system-value semantic, and compatibility-mode combination.

The source catalogue includes retrieval evidence, not proof every upstream claim has been independently tested. Sample index values are observations from one translation package; they must be verified against any other game before modification.
