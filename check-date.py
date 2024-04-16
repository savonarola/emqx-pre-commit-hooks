#!/bin/env python3

import datetime
import re
import sys

CHEKS = [
    (r"\bBSL.txt$", r"The Licensed Work is"),
    (r"\.erl$", r"^%% Copyright")
]

def check_files(files, year):
    for filename in files:
        yield from check_date(filename, year)


def check_date(filename, year):
    for filename_pattern, year_pattern in CHEKS:
        if re.search(filename_pattern, filename):
            with open(filename) as f:
                content = f.read()
                result, line = check_content(content, year_pattern, year)
                if not result:
                    yield(f"{filename}:\n--->{line}")


def check_content(content, year_pattern, year):
    lines = content.split("\n")
    for line in lines:
        if re.search(year_pattern, line):
            if not re.search(str(year), line):
                return (False, line)
    return (True, None)

def current_year():
    today = datetime.date.today()
    year = today.year
    return year

if __name__ == '__main__':
    year = current_year()
    filenames = sys.argv[1:]

    errors = list(check_files(filenames, year))

    if errors:
        print(f"Date is not updated in {len(errors)} file(s)")
        for error in errors:
            print(error)
        sys.exit(1)



