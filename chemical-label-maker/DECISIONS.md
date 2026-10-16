# Decision log

Who decided what, and why. Entries marked **User** were the user's call; **Proposed** entries are Claude's suggestions awaiting a decision.
Newest at the bottom.

## 2026-10-16

| # | Decision | Decided by | Reasoning |
|---|---|---|---|
| 1 | Build as Word/VBA in a `.docm` | User (handover) | Runs on school laptops with limited install rights; other technicians can use it. |
| 2 | Tool stores only wording and rules, never chemical data | User (handover) | Names, concentrations and classifications go out of date. |
| 3 | Phrase library starts empty; grows from real use | User (handover) | No pre-seeded list that could go stale. |
| 4 | Phrase library lives inside the document (no second file), starting with a hidden end section | User | Avoids two files drifting apart. |
| 5 | Library access goes through `LoadPhrases` / `SavePhrases` only, so storage can later move to a custom XML part | User (direction), Claude (shape) | User wants it to run without them on hand to fix it; switching later must touch one module. |
| 6 | Label sizes are named presets in a settings table, chosen from a dropdown; no fixed size yet | User | Sizes not decided; will be set from existing Word files and a test print. |
| 7 | Source is plain-text VBA modules in the repo, imported into the `.docm`; user does not edit code | User (direction) | User does not want to work in the VBA editor. |
| 8 | Hazcards are used only to cross-check the worked examples; no hazcard data enters the repo | User (principle), Claude (rule) | Matches decision 2. |
| 9 | Work proceeds in small steps, with a check-in on each decision | User | User wants to direct the work, and to be able to show it. |
| 10 | If a chosen pictogram always carries DANGER, the header suggestion is DANGER, whatever else is chosen | User | "That one will always win." Which pictograms qualify is still being confirmed (see rule table below). |
| 11 | If none of the chosen pictograms is always-DANGER, the suggestion is blank, except where the examples show WARNING (see open question A) | User | Some pictograms can carry either word depending on the chemical, so the tool must not guess. |
| 12 | No pictograms: header is blank (no WARNING or DANGER) | User | Usually means not classified as hazardous (e.g. 0.1 M HCl). The label still identifies the chemical; CLEAPSS eye protection wording is a bullet, not a header. |
| 13 | The header suggestion is shown as the default and the user may change it at any time; no forced confirmation step | User (replaces Claude's lean towards always confirming) | Closes the handover's open question on header confirmation. |

## Header rule: working table (draft, needs confirming)

| Pictograms chosen | Suggested header | Status |
|---|---|---|
| None | blank | Decided (12) |
| Corrosion (GHS05), with or without anything else | DANGER | Decided (10), matches handover |
| Exclamation mark (GHS07) only | WARNING | In handover and worked examples; unclear against decision 11 (question A) |
| Exclamation mark + a pictogram that can carry either word | ? | Question A |
| Skull (GHS06) or Health hazard (GHS08) only | blank | Handover: either word possible |
| Explosive, Flammable, Oxidising, Gas cylinder, Environment | ? | Not covered by the handover (question B) |
