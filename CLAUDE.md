# Science technician tools

Tools for a school science technician. Currently one project: `chemical-label-maker/`, a Word/VBA hazard label maker. Start with `chemical-label-maker/first-laptop-session.md`.

## How to work with this user

- **They direct; you propose.** The user wants to make the decisions and be able to show the work as directed by them. Do not decide design questions silently. For each real decision, give a recommendation with the trade-off, wait for their answer, then record it in `chemical-label-maker/DECISIONS.md` (number, who decided, why).
- **Small steps, check in often.** Describe each slice of work in plain English and get a yes before building it. Stop after each slice and show the result.
- **The user does not edit or read VBA.** They dislike working in the VBA editor. Keep all code in plain-text files in the repo and do the importing, running and fixing yourself. Describe behaviour to them, not code.
- **Say what you could not verify.** Never present unrun VBA as working. Report test failures with the output.
- Do not guess at chemical or safety facts. The user checks classifications against CLEAPSS hazcards by hand.

## Rules that must not be broken

- The tool stores only wording (the phrase library). No chemical names, concentrations, units, classifications or signal-word rules (`DECISIONS.md` 2, 14).
- No hazcard content goes into the repo (decision 8).
- The phrase library lives inside the Word document; never a second file (decision 4).
- The header (DANGER / WARNING / none) is always chosen by the user, never defaulted (decision 14).

## Checks

- `python3 -I chemical-label-maker/tests/check_phrase_logic.py chemical-label-maker/tests/phrase-library-cases.txt` runs the phrase library rules. It is a throwaway Python mirror of the design; the VBA module must pass the same cases file.
