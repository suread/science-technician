# Form specification (v1) - DRAFT for review

Plain-English description of the one screen the user fills in. Nothing here is built yet.
Items marked **Proposed** are Claude's suggestions and have not been agreed. Everything else follows `DECISIONS.md`.

## The screen, top to bottom

1. **Chemical name.** A text box. Required. Printed in capitals and bold on the label (decision 26), whatever case it was typed in.

2. **Concentration.** A value box and a unit dropdown, side by side. Both empty for a solid (decision 27).
   - The value box takes text, not only numbers, because bands such as `0.2-1` are needed.
   - The unit dropdown holds a fixed list: M, vol, % w/v, % v/v (decision 30).
   - **Proposed:** a value with no unit, or a unit with no value, is flagged before the label can be built.

3. **Dot colour.** Three radio buttons: red (acid), blue (alkali), none. Default none. Display only; it does not filter anything.

4. **Pictograms.** Nine tick boxes, each with the small picture and its name (decision 28). Ticking none is valid.

5. **Header.** A dropdown the user must set on every label (decision 14).
   - It starts on a prompt, "Choose...", then offers DANGER, WARNING and "None (no header)" (decision 31). The Preview button stays inactive while it still says "Choose..." or the chemical name is empty. Without that starting state there would be no way to tell "the user chose none" from "the user hasn't looked yet".

6. **Hazard bullets.** A list of bullet lines. For each bullet the user types in a search box, picks from the matching phrases, or picks "Add new phrase..." (decisions 17, 19-25).
   - The user can add more bullets and remove one.
   - **Proposed:** bullets print in the order added.
   - The maximum number of bullets depends on label size; see Open questions.

7. **Buttons.** Preview, and Cancel.

## After the form

1. **Preview.** One label shown in each layout, side by side: pictograms in a row with text underneath, and pictograms in a column with text to the right.
2. **Pick a layout.** The choice is per label and is not remembered against the chemical.
3. **Build the sheet.** A full A4 sheet of repeats in that layout.
4. **Export to PDF.** The PDF is what gets reprinted; the tool is not used again for the same label.
5. New phrases typed during the form are saved to the library now, not before (decision 25).

## Open questions (to settle before building the form)

- **Unknown concentration.** Some exercises have the student work out the concentration, so lower school labels read "acid X", "acid Y" with no concentration. With the current form this already works: leave value and unit both empty, same as a solid. Open: whether a label for A-level needs anything different. The user is checking with a colleague.
- **Label sizes.** Not decided. To be read from existing Word label files, then confirmed with a test print (decision 6). This also fixes the maximum number of bullets.
- **How name and concentration sit together** on the label, e.g. `SODIUM HYDROXIDE 0.4 M` on one line or on two. To be tried in the layout prototype.
