#!/bin/env python3

import fnmatch
import os
import shlex
import sys

FORMAT_FILES = [
    "*.app.src",
    "*.erl",
    "*.hrl",
    "rebar.config",
    "*.eterm",
    "*.escript",
    "rebar.config.script",
    "elvis.config",
    "nodetool"
]

FMT_SCRIPT = "./scripts/erlfmt"

def format_file(filename):
    print(f"Formatting: {filename}")
    os.system(f"{FMT_SCRIPT} -w {shlex.quote(filename)}")

def need_format(filename):
    for pattern in FORMAT_FILES:
        if fnmatch.fnmatch(os.path.basename(filename), pattern):
            return True
    return False

def main():
    filenames = sys.argv[1:]

    for filename in filenames:
        if not need_format(filename):
            continue
        format_file(filename)
    return 0


if __name__ == '__main__':
    raise SystemExit(main())