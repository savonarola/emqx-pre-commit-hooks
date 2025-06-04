#!/bin/env python3

import re
import sys

PATTERN = r"\b\.erl$"
MACRO_PATTERN = r"\-define\((.+?)\b"

def check_files(files):
    for filename in files:
        yield from check_file(filename)


def check_file(filename):
    if re.search(PATTERN, filename) and not re.search(r"\b_build/", filename):
        with open(filename) as f:
            content = f.read()
            yield from check_content(filename, content)


def check_content(filename, content):
    lines = content.split("\n")
    macros = []
    for lineno, line in enumerate(lines):
        line_macros = re.findall(MACRO_PATTERN, line)
        for macro in line_macros:
            macros.append((lineno + 1, macro))
    for lineno, macro in macros:
        macro_usage_pattern = rf"\?{macro}\b"
        if not re.search(macro_usage_pattern, content):
            yield (filename, lineno, macro)


def main():
    filenames = sys.argv[1:]

    errors = list(check_files(filenames))

    if errors:
        print(f"Unused macros: {len(errors)}")
        for (filename, lineno, macro) in errors:
            print(f"{filename}:{lineno}: {macro}")
        return 1
    else:
        return 0


if __name__ == '__main__':
    raise SystemExit(main())