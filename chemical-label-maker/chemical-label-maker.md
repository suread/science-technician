# Chemical Hazard Label Maker: Handover (updated 16 Oct 2026)

> **Note (16 Oct 2026):** where this handover and `DECISIONS.md` differ, `DECISIONS.md` wins. Changed so far: the header is chosen by the user every time (no pictogram-based rule, see decisions 14-15); the phrase library has no pictogram tags, so the line format is one phrase per line and the phrase list is filtered only by typed words, sorted alphabetically (decisions 16-17); the library lives in the document with no second file (decision 4).

## What this is

A Word/VBA tool that produces an A4 sheet of repeating hazard label blocks for printing and cutting. Each block is taped onto a small container sent out to classes. These are not adhesive labels.

It replaces a manual process: a Word table, edited by hand for each new chemical or concentration, with past versions kept for reuse.

## Core design principle

The tool stores only wording and the rules that link it to pictograms. It does not store chemical names, concentrations, units, or hazard classifications. These change over time, and the tool must not hold data that goes out of date.

Each label is built from fresh entries each time:

- Chemical name
- Concentration and unit (blank for solids)
- Dot colour
- Pictograms
- Header (WARNING or DANGER)
- Hazard bullets

The tool stores:

- The phrase library, each phrase tagged with the pictograms it has been used with
- The pictogram-to-header rule (see below)

Chemical classifications come from CLEAPSS hazcards, which the user checks by hand. Hazcards are not inputs to the tool.

## What each label needs

- **Chemical name.** Shown capitalised.
- **Concentration and unit.** Value typed, unit chosen from a dropdown. Units include M, vol (for peroxide), and % w/v (for example starch). Solids have no unit. The tool must not assume molarity.
- **Dot colour.** Radio button: red (acid), blue (alkali), or none. Default is none. It is a display choice only, not a filter. Acid and alkali are too broad to use as a filter.
- **Pictograms.** Multiple selection from nine GHS pictograms. "None" is a valid choice.
- **Header.** Dropdown: WARNING, DANGER, or none. The tool suggests one from the pictograms; the user confirms.
- **Hazard bullets.** Chosen from the phrase library or typed as new text.

## Header rule

The header follows the pictograms chosen, as far as the examples so far show:

- Corrosion (GHS05) present: DANGER.
- Exclamation mark (GHS07) only: WARNING.
- Corrosion and exclamation mark together: DANGER.
- Toxic and health-hazard pictograms (GHS06, GHS08) can carry either word. The tool leaves the header blank for these and asks the user.

The rule is a suggestion. The user always confirms the header.

## Pictogram source

Standard GHS pictograms from **Wikimedia Commons**, category "GHS pictograms". The files are public domain (checked by the user on the Commons page). Use these SVG files:

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

## Hazard statements

The GitHub statements source (hpstatements) is **no longer used**. Phrases are added as labels are made, so the library grows from real use. The CLEAPSS hazcard remains the reference for label content.

## Phrase library

- Starts empty. No pre-seeded list.
- A phrase is saved the first time it is used, tagged with the pictograms chosen at that point.
- When pictograms are selected, the phrase list shows matching phrases first.
- Typing narrows the list (for example, typing "irrit" shows phrases containing "irritant" or "irritation"). Matches are limited to phrases tagged with the chosen pictograms.
- Free text is always available for new phrases.
- Dot colour does not filter the phrase list.

## Where to store the phrase library

The library must live in the Word document, shared between technicians. Options:

**1. Hidden section at the end of the document (recommended for a first version)**
- Pros: Simple to build. One file. The contents are visible if something goes wrong. Easy to edit by hand. Another technician can read it.
- Cons: Someone typing into the body can break it. Needs a clear marker and a warning on the form.

**2. Custom document property or custom XML part**
- Pros: Hidden from users and hard to break by accident. Can be read and written by VBA.
- Cons: More code to maintain. Harder for another technician to inspect or repair. Less obvious where the data lives.

**3. Separate plain text file beside the document**
- Pros: Easiest to back up and share. Readable by any tool. Simple to edit.
- Cons: Two files must stay together. Risk of the document and the file getting out of step.

Line format for option 1 (and option 3):

    Wear eye protection<TAB>GHS07
    Causes skin irritation<TAB>GHS07

The document must be saved as a macro-enabled file (.docm). Macros are known to work on the school laptop from earlier VBA use in Excel.

## Confirmed flow

1. Fill in the form: name, concentration and unit, dot colour, pictograms, header, bullets.
2. The tool shows a one-label preview in each layout style, side by side.
3. The user picks a layout.
4. The tool builds the full A4 sheet of repeats in that layout.
5. Export as PDF. This PDF is the reusable artifact. Reprint from it rather than rebuilding.

The chosen layout is not saved against the chemical. The same chemical may need different layouts for different containers.

## Layout options

- Row of pictograms, text underneath.
- Column of pictograms, text to the right.

Layout is not derived automatically from pictogram count. The user chooses per label.

## Build approach

Word/VBA. Reasons:

- It has to run on a school laptop with limited install rights. VBA inside Word already works there.
- The school uses Microsoft tools, and other technicians need to be able to use it.

The repo for lab-technician tools will hold this tool with its docs alongside it.

## Open questions

- Storage option for the phrase library (see above).
- Exact VBA implementation: userform layout, how the two previews are rendered side by side, how the phrase list is read and written.
- Whether the pictogram library is all nine standard images or only those the school uses.
- Whether the header should always be confirmed, or can be accepted automatically when it matches the rule.

## Worked examples (research sample, not tool data)

| Chemical | Concentration | Pictograms | Header |
|---|---|---|---|
| Sodium hydroxide | 0.4 M | Exclamation mark | WARNING |
| Sodium hydroxide | 0.2–1 M (per hazcard band) | Corrosion | DANGER |
| Copper(II) sulfate | 1 M | Corrosion and exclamation mark | DANGER |
| Hydrogen peroxide | 20 vol | Exclamation mark | WARNING |

These are used only to test the header rule. The tool does not store them.

## Not yet done

- Confirm the hydrogen peroxide and other remaining sample chemicals against their hazcards.
- Choose the storage option for the phrase library.
- VBA implementation.
