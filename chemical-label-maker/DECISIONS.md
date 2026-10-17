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
| 10 | **Parked pending research (see 14).** If a chosen pictogram always carries DANGER, the header suggestion is DANGER, whatever else is chosen | User | "That one will always win." Which pictograms qualify is still being confirmed (see rule table below). |
| 11 | **Parked pending research (see 14).** If none of the chosen pictograms is always-DANGER, the suggestion is blank, except where the examples show WARNING (see open question A) | User | Some pictograms can carry either word depending on the chemical, so the tool must not guess. |
| 12 | No pictograms: header is typically empty, though the user still chooses (see 14) | User | Usually means not classified as hazardous (e.g. 0.1 M HCl). The label still identifies the chemical; CLEAPSS eye protection wording is a bullet, not a header. |
| 13 | **Replaced by 14.** The header suggestion is shown as the default and the user may change it at any time; no forced confirmation step | User (replaces Claude's lean towards always confirming) | Closes the handover's open question on header confirmation. |
| 14 | The header is a required choice on every label: DANGER, WARNING or empty. No default is suggested from the pictograms in the first version. | User | Which pictograms imply which signal word is unverified, and the user will need to choose by hand in some cases anyway. A forced choice means the tool never makes a safety call for the user. |
| 15 | Pictogram-based header defaults may be added later, once the signal word for each pictogram and category is verified against a primary source (UN GHS Annex 3 or EU CLP) | User | Parked, not rejected. |
| 16 | The phrase library has no pictogram tags. It is a plain list of unique phrases. | User | Tags would drift: a phrase used once on an unusual chemical would stay associated with the wrong pictogram. Typed-word filtering gets to a short list quickly without them. |
| 17 | The phrase list is filtered only by the words typed, and is sorted alphabetically | User | "Splashproof" is more defining than "wear". Without tags there is nothing else to order by. |
| 18 | Editing and deleting phrases (typo repair) is wanted but is not in v1 | User | Keeps v1 small. |
| 19 | Provisional matching details: case-insensitive; typed text matches anywhere inside a phrase ("irrit" finds "irritant" and "irritation"); several typed words must all appear, in any order; a phrase already in the library (ignoring case and extra spaces) is not saved twice | Claude (proposed), User confirmed | Small details that follow from 16-17. |
| 20 | Multi-word matching (all words, any order) is included in v1 | User | Started as a nice-to-have; the code is only a few lines, so it goes in. |
| 21 | If a phrase already exists (ignoring case and extra spaces), the original wording is kept. Corrections are made through the later edit/delete feature. | User | Keeps the library predictable; wording changes should be deliberate. |
| 22 | `*` and `?` are ordinary characters when typing in the phrase search. No wildcard searching. | User | Unnecessary complication for non-IT users, and `*` may legitimately appear on a label. |
| 23 | Adding a new phrase is a deliberate option in the phrase list ("Add new phrase..."), not "whatever is in the search box". The search text is not used as the new phrase. | User | Search wording (e.g. "goggles splash") is not the proper phrase; the user wants to type the full wording on purpose. |
| 24 | "Add new phrase..." is always the first entry in the phrase list, unaffected by filtering, shown differently from real phrases (e.g. in brackets). A phrase with that exact text cannot be saved. | User (agreed Claude's proposal) | It must be visible exactly when a search finds nothing, and must not be mistaken for a phrase. |
| 25 | A new phrase is added to the current label immediately but saved to the library only when the label is built. | User (agreed Claude's proposal; either option was acceptable) | Matches the handover ("saved the first time it is used") and abandoned labels do not leave typos in the library. Cost: a new phrase is lost if Word closes before the sheet is built. Revisit if that bites. |
| 26 | The chemical name is printed in capitals and bold (e.g. **SODIUM HYDROXIDE**) | User | Contrasts with the hazard/precaution text; bold separates it from the header, which is also usually capitals. |
| 27 | Concentration units come from a fixed dropdown; users cannot type their own. Solids have no concentration and no unit. | User | Safer than free text. Exact list to be confirmed (see form-spec.md). |
| 28 | All nine GHS pictograms are offered | User | The CLEAPSS pictogram macro the school uses also offers all nine. |
| 29 | Both the home and work laptops are Windows 11. Only the home laptop will be used for Claude Code sessions driving Word. | User | The work laptop is used for running the finished tool, not for development. |
| 30 | The unit list is M, vol, % w/v and % v/v, and nothing else for v1. Concentrations by mass are expressed as % w/v, not g/L. | User | The school has a standard way of expressing concentration in %, and the conversion is minimal. (1 % w/v = 10 g/L, so the two must not be mixed up.) % v/v added in case liquid enzymes are bought in place of powders. |
| 31 | The header dropdown starts on "Choose..." (a prompt, not a header value). The button that moves on from the form stays inactive until a header has been chosen. | User (agreed Claude's proposal) | Makes the choice forced, and separates "chose none" from "hasn't looked yet". |
| 32 | On the label, the concentration is the top line and the chemical name the line below it, both centred (as on current labels). With no concentration (solids, "acid X"), only the name line appears. | User | Keeps the familiar look. |
| 33 | Bullets are never dropped or limited to fit. Label height grows with the content instead. | User | "If they are needed, they are needed." Consequence: the number of label rows per A4 sheet is worked out from the label height, not fixed. |
| 34 | Label width is fixed by the chosen preset. Long text wraps, and the font size may be reduced to help. If a single label is taller than the sheet, the tool warns and does not build. | User | Container sizes are fixed. Rules for reducing the font (automatic or chosen, and the smallest allowed size) are not decided; see open items. |
| 35 | The concentration line and the name line are the same size and both bold | User | Matches the user's preference; to be checked against existing labels. |
| 36 | `form-spec.md` has been read by the user and is accepted as the basis for the build, with the open questions listed in it still to settle | User | Handover to the next session. |
| 37 | While the user is the only person using the tool, the phrase library section stays visible in the document (clearly marked, not hidden), and updates to the tool are handled by informal versioning (several file names) and copying the phrase text into the new `.docm` by hand. Hiding the section, or moving it to a custom XML part, waits until other technicians use the tool. | User | Hiding the phrases makes manual copying harder, and the user is the only user for now. This also removes the urgency of the "update without wiping the library" open item. Refines decisions 4 and 5. |

## Open items for the next session

- **Font reduction.** When and how far may text shrink to fit a label (decision 34)? Not decided.
- **Label size presets.** Width and columns, read from the user's existing Word label files and confirmed by a test print (decision 6).
- **Updating a deployed document without losing the phrase library.** Not urgent while the user is the only user (decision 37); needed before others use it. The library lives inside the `.docm` that technicians use (decision 4), so rebuilding that file from the source modules would wipe it. The import step must replace the code in an existing document and leave the library section alone, or the library must be exported and re-imported around an update. Needs a design before the first release.
- **Signal word research** (below).
- **Unknown concentration** for A-level (see `form-spec.md`).

## Research to do (not started)

Verify against a primary source, then record the result here:

- Signal word(s) allowed for each of GHS01-GHS09, by hazard class and category.
- Whether Corrosion (GHS05) can carry WARNING (for example corrosive to metals, H290). This affects the old "corrosion always wins" idea (10).
- Whether Skull (GHS06) can carry WARNING. The handover says it can; the research may disagree.
- Whether Environment (GHS09) carries no signal word in some categories.

The sandbox could not reach the reference sites (network policy), so this is best done in a laptop session using the Chrome extension, or after allowing the hosts.
