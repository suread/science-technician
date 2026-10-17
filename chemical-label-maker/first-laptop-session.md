# First laptop session: where to start

Written 17 Oct 2026 at the end of the cloud design sessions. The user's home laptop is Windows 11 with their own Microsoft 365 subscription, and they have admin rights. The work laptop will only be used to run the finished tool, not to develop it.

Read `../CLAUDE.md` (how to work with this user), `DECISIONS.md` (36 decisions so far), `form-spec.md` and `chemical-label-maker.md` first.

## Before starting (the user)

- Clone the repo and check out the branch `label-maker-vba-v1`.
- Have Word (desktop, Microsoft 365) installed.
- Bring one or two existing label files (Word) if possible, so the label sizes, fonts and spacing can be read from them.
- In Word: File > Options > Trust Center > Trust Center Settings > Macro Settings, and tick **Trust access to the VBA project object model**. Without this, code cannot be imported into a document from outside Word.
- Keep working files in a folder Word treats as trusted (Trust Center > Trusted Locations), so macros are not blocked.

## Suggested order of work

Check in with the user on each step; they want to direct it.

1. **Prove the loop.** Write a small script (PowerShell with the Word COM object, or Python with pywin32; propose which) that creates a `.docm`, imports a VBA module, runs a macro and reads a result back. Everything after depends on this, so do it before any real code.
2. **Read the existing label files.** Unzip the `.docx` or inspect it through Word to find the table sizes, fonts, spacing and how the concentration and name are styled. Propose label size presets (width and columns) and get the user's yes. Check decision 35 (same size, both bold).
3. **Slice 1 in VBA: the phrase library.** Plain-English description first, then the module. Include a self-test macro that runs `tests/phrase-library-cases.txt` inside Word, so Python and VBA are held to the same cases. Mind the wildcard trap: use `InStr`, not `Like` (decision 22).
4. **Slice 2: the form**, from `form-spec.md`. Build the controls in code (not the visual designer) so the whole form is plain text.
5. **Slice 3: the preview and the sheet**, including the two layouts, the growing label height (decision 33), the "too tall" warning (decision 34) and the PDF export.
6. **Test print** a real sheet, cut it, and tape it on a container. Only the user can judge this.

## Things to settle during the session

See "Open items for the next session" in `DECISIONS.md`. In particular:

- Label size presets, and how and when the font may shrink.
- **Updating a deployed document without wiping the phrase library** (the library is inside the `.docm`). Design this before the first release.
- A-level concentration labelling (the user is checking with a colleague).

## Separate piece of research (can be its own session)

Verify, from a primary source (UN GHS Annex 3 or EU CLP), which signal words each pictogram and hazard category can carry. The cloud session could not reach those sites. Use the Claude in Chrome extension (`claude --chrome`) on the user's own browser. Findings go in `DECISIONS.md`. Only after that, and only if the user agrees, could pictogram-based header defaults be added (decision 15).

## Expectations

- VBA written without running will have errors. With the loop from step 1, fix your own errors rather than asking the user to paste them.
- The cloud sandbox could not run Word. Nothing in `tests/` proves the VBA works, only that the design is consistent.
