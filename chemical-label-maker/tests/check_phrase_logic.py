"""Throwaway Python mirror of the phrase library rules, run against phrase-library-cases.txt.

This checks the design (DECISIONS.md 16-23). It is not the product; the product is the VBA module,
which must pass the same cases file.
"""
import sys
from pathlib import Path


def normalise(text):
    return " ".join(text.split())


def filter_phrases(library, typed):
    words = typed.lower().split()
    hits = [p for p in library if all(w in p.lower() for w in words)]
    return sorted(hits, key=str.lower)


def add_phrase(library, phrase):
    clean = normalise(phrase)
    if not clean:
        return list(library)
    if any(normalise(p).lower() == clean.lower() for p in library):
        return list(library)
    return list(library) + [clean]


def field(text):
    text = text.strip()
    if len(text) >= 2 and text[0] == '"' and text[-1] == '"':
        return text[1:-1]
    return text


def phrase_list(text):
    text = field(text)
    return [p.strip() for p in text.split(";") if p.strip()]


def main(path):
    failures = passed = 0
    for number, line in enumerate(Path(path).read_text().splitlines(), 1):
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        parts = line.split("|")
        kind, name = parts[0].strip(), parts[1].strip()
        library = phrase_list(parts[2])
        if kind == "FILTER":
            actual = filter_phrases(library, field(parts[3]))
        elif kind == "ADD":
            actual = add_phrase(library, field(parts[3]))
        else:
            print(f"line {number}: unknown kind {kind!r}")
            failures += 1
            continue
        expected = phrase_list(parts[4])
        if actual == expected:
            passed += 1
        else:
            failures += 1
            print(f"FAIL line {number}: {name}\n  expected {expected}\n  actual   {actual}")
    print(f"{passed} passed, {failures} failed")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1] if len(sys.argv) > 1 else Path(__file__).with_name("phrase-library-cases.txt")))
