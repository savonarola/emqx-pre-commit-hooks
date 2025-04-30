#!/bin/env python3

import pathlib
import re
import sys

PATTERN = r"\b.md$"
MD_LINK_PATTERN = r"\[.*?\]\((.*?)\)"

def check_files(files):
    for filename in files:
        yield from check_file(filename)


def check_file(filename):
    if re.search(PATTERN, filename):
        with open(filename) as f:
            content = f.read()
            yield from check_content(filename, content)


def check_content(filename, content):
    lines = content.split("\n")
    for lineno, line in enumerate(lines):
        links = re.findall(MD_LINK_PATTERN, line)
        for link in links:
            if is_local_link(link):
                full_link = pathlib.Path(filename).parent / remove_anchor(link)
                if not full_link.exists():
                    yield (filename, lineno, full_link)

def is_local_link(link):
    return not re.match(r"^\w+?://", link) and not re.match(r"^todo$", link, re.IGNORECASE)

def remove_anchor(link):
    return re.sub(r"#.*$", "", link)


def main():
    filenames = sys.argv[1:]

    errors = list(check_files(filenames))

    if errors:
        print(f"Local links not found: {len(errors)}")
        for (filename, lineno, full_link) in errors:
            print(f"{filename}:{lineno}: {full_link}")
        return 1
    else:
        return 0


if __name__ == '__main__':
    raise SystemExit(main())