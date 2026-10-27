#!/usr/bin/env python3
"""JobSearchOS filename sync.

Keeps the status prefix of every file in jobs/ in line with the `status:` field in
its dossier's frontmatter. Works with any AI tool because it uses no AI at all.

Usage:
  python3 sync-filenames.py /path/to/your/job-search-folder            # dry run, prints changes
  python3 sync-filenames.py /path/to/your/job-search-folder --apply    # renames files

Rules (same as /log-application sync):
  shortlisted            -> no file yet, skipped
  researched, drafted    -> 3-
  applied                -> 2-
  screening, task        -> 1-
  offer                  -> 0-
  rejected/ghosted/killed-> zz-
Skips _TEMPLATE.md, anything starting with DEPR-, and any DEPR-* folder.
Only renames. It never edits file contents and never deletes anything.
"""
import re
import sys
from pathlib import Path

PREFIX = {
    "researched": "3-", "drafted": "3-",
    "applied": "2-",
    "screening": "1-", "task": "1-",
    "offer": "0-",
    "rejected": "zz-", "ghosted": "zz-", "killed": "zz-",
}
KNOWN = ("0-", "1-", "2-", "3-", "zz-")
SUFFIXES = ("-letter.html", "-resume.html", "-email.md", "-screening-prep.md", ".md")


def read_status(md: Path):
    text = md.read_text(encoding="utf-8", errors="replace")
    m = re.match(r"^---\s*\n(.*?)\n---", text, re.S)
    if not m:
        return None
    s = re.search(r"^status:\s*([A-Za-z-]+)", m.group(1), re.M)
    return s.group(1).strip().lower() if s else None


def split_prefix(name: str):
    for p in KNOWN:
        if name.startswith(p):
            return p, name[len(p):]
    return "", name


def slug_of(rest: str):
    for suf in SUFFIXES:
        if rest.endswith(suf):
            return rest[: -len(suf)], suf
    return None, None


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)
    root = Path(sys.argv[1]).expanduser() / "jobs"
    apply = "--apply" in sys.argv
    if not root.is_dir():
        print(f"No jobs/ folder at {root}")
        sys.exit(1)

    dossiers = [p for p in root.glob("*.md")
                if p.name != "_TEMPLATE.md" and not p.name.startswith("DEPR-")]
    wanted = {}  # slug -> (status, wanted prefix)
    for md in sorted(dossiers):
        pfx, rest = split_prefix(md.name)
        slug, suf = slug_of(rest)
        if slug is None or suf != ".md":
            continue  # a companion .md such as -email.md, handled with its dossier
        status = read_status(md)
        if status is None or status == "shortlisted" or status not in PREFIX:
            continue
        wanted[slug] = (status, PREFIX[status])
    checked = len(wanted)
    changes = []
    # Check every file, so a companion file that kept an older prefix is fixed too.
    for f in sorted(root.iterdir()):
        if not f.is_file() or f.name.startswith("DEPR-") or f.name == "_TEMPLATE.md":
            continue
        pfx, rest = split_prefix(f.name)
        slug, _ = slug_of(rest)
        if slug not in wanted:
            continue
        status, want = wanted[slug]
        if pfx == want:
            continue
        new = root / f"{want}{rest}"
        if new.exists():
            print(f"SKIP (target exists): {f.name} -> {new.name}")
            continue
        changes.append((f, new, status))

    for old, new, status in changes:
        print(f"{old.name} -> {new.name}   (status: {status})")
        if apply:
            old.rename(new)

    if not changes:
        print(f"Checked {checked} dossiers, all filenames match their status, nothing to do.")
    elif not apply:
        print(f"\n{len(changes)} rename(s) pending. Re-run with --apply to do them.")
    else:
        print(f"\nRenamed {len(changes)} file(s).")


if __name__ == "__main__":
    main()
