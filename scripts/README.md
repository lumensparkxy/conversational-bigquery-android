# Specification validation

Run `python3 scripts/validate_specs.py` from the repository root using Python 3. This dependency-free check validates required files, nonempty planned-folder READMEs and relative Markdown file links, and rejects obvious credential artifact names outside ignored work/git directories. It does not validate external links, anchor fragments, application correctness or absence of every possible secret. Review content before publishing. No application CI exists yet.
