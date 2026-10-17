# Chemical Hazard Label Maker: Handover (updated 17 Oct 2026)

This file describes what the tool is. **`DECISIONS.md` is the log of what has been decided and why, and wins where the two differ.** `form-spec.md` describes the one screen the user fills in. `first-laptop-session.md` says where to start.

## What this is

A Word/VBA tool that produces an A4 sheet of repeating hazard label blocks for printing and cutting. Each block is taped onto a small container sent out to classes. These are not adhesive labels.

It replaces a manual process: a Word table, edited by hand for each new chemical or concentration, with past versions kept for reuse.

## Core design principle

The tool stores only wording. It does not store chemical names, concentrations, units, hazard classifications or signal-word rules. These change over time, and the tool must not hold data that goes out of date.

Each label is built from fresh entries each time. The only thing stored is the **phrase library**: a plain list of unique hazard/precaution phrases, with no pictogram tags.

Chemical classifications come from CLEAPSS hazcards, which the user checks by hand. Hazcards are not inputs to the tool and no hazcard content goes in this repo.

## What each label has

- **Concentration** (top line) and **chemical name** (line below), both centred, same size, both bold. The name is in capitals. With no concentration (solids, or exercises where students find it), only the name line appears.
- **Concentration** is a text value plus a unit from a fixed list: M, vol, % w/v, % v/v. Value and unit are both empty for solids. The tool never assumes molarity.
- **Dot colour:** red (acid), blue (alkali) or none (default none). Display only.
- **Pictograms:** any of the nine GHS pictograms, or none.
- **Header:** DANGER, WARNING or none, chosen by the user every time. The tool offers no default. The dropdown starts on "Choose..." and the user cannot continue until a choice is made.
- **Hazard bullets:** chosen from the phrase library or typed as new text. No limit; the label grows taller.

## Pictogram source

Standard GHS pictograms from **Wikimedia Commons**, category "GHS pictograms". The files are public domain (checked by the user on the Commons page). They are in `pictograms/`:

| Pictogram | File |
|---|---|
| Explosive (GHS01) | GHS-pictogram-explos.svg |
| Flammable (GHS02) | GHS-pictogram-flamme.svg |
| Oxidising (GHS03) | GHS-pictogram-rondflam.svg |
| Gas cylinder (GHS04) | GHS-pictogram-bottle.svg |
| Corrosion (GHS05) | GHS-pictogram-acid.svg |
| Skull and crossbones (GHS06) | GHS-pictogram-skull.svg |
| Exclamation mark (GHS07) | GHS-pictogram-exclam.svg |
| Health hazard (GHS08) | GHS-pictogram-silhouette.svg |
| Environment (GHS09) | GHS-pictogram-pollu.svg |

Do not use the "question mark" file in the same category; it is Wikipedia-internal only.

Word on Microsoft 365 handles SVG insertion and resizing. If the tool is run on an older Office version, convert to PNG at about 400 px.

## Phrase library

- Starts empty. No pre-seeded list. Phrases are added as labels are made.
- A plain list of unique phrases. One phrase per line, no tabs or tags.
- The list is filtered only by what the user types, and sorted alphabetically. Matching ignores case, matches anywhere inside a phrase, and needs every typed word to appear (in any order). `*` and `?` are ordinary characters.
- "Add new phrase..." is always the first entry in the list. The text in the search box is never used as the new phrase.
- A phrase that already exists (ignoring case and extra spaces) is not saved again, and the original wording is kept.
- A new phrase is added to the current label at once, and saved to the library when the label is built.
- Editing and deleting phrases (typo repair) is wanted but is not in v1.
- Dot colour and header do not filter the phrase list.

The exact rules are in `tests/phrase-library-cases.txt`, checked by `tests/check_phrase_logic.py`.

### Where it is stored

Inside the Word document, so there is never a second file: a hidden section at the end of the document, to start with. All reads and writes go through two procedures, `LoadPhrases` and `SavePhrases`, so the storage can later move to a hidden custom XML part without touching anything else. The long-term aim is that the tool runs without the original author being on hand to fix it, so the library needs a clear marker, validation on write, and a timestamped backup before each save.

The document must be saved as a macro-enabled file (`.docm`). Macros are known to work on the school laptop from earlier VBA use in Excel.

## Confirmed flow

1. Fill in the form (see `form-spec.md`).
2. The tool shows a one-label preview in each layout style, side by side.
3. The user picks a layout. It is not saved against the chemical.
4. The tool builds the full A4 sheet of repeats in that layout.
5. Export as PDF. This PDF is the reusable artifact. Reprint from it rather than rebuilding.

## Layout options

- Row of pictograms, text underneath.
- Column of pictograms, text to the right.

Layout is not derived from pictogram count. The user chooses per label.

Label **width** is fixed by a named size preset; **height** grows with the content and the number of rows on the sheet is worked out from it. Sizes are not decided yet.

## Build approach

Word/VBA, because it has to run on a school laptop with limited install rights and other technicians need to be able to use it.

Source is plain-text VBA modules kept in this repo, imported into a `.docm`. The user does not edit code and does not want to work in the VBA editor. Development happens in Claude Code sessions on the user's own Windows 11 laptop, where Word can be driven from the command line to import, run and check. Cloud sessions can write and check the rules but cannot run Word.

## Worked examples (research sample, not tool data)

Useful as test labels for previews and layouts. The header is the user's choice each time, so these are no longer used to test a rule.

| Chemical | Concentration | Pictograms | Header |
|---|---|---|---|
| Sodium hydroxide | 0.4 M | Exclamation mark | WARNING |
| Sodium hydroxide | 0.2-1 M (per hazcard band) | Corrosion | DANGER |
| Copper(II) sulfate | 1 M | Corrosion and exclamation mark | DANGER |
| Hydrogen peroxide | 20 vol | Exclamation mark | WARNING |
| Hydrochloric acid | 0.1 M | none | none |

## Not yet done

Everything beyond the phrase library rules. See `DECISIONS.md` ("Open items for the next session" and "Research to do") and `first-laptop-session.md`.
