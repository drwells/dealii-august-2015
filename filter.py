#!/usr/bin/env python
"""
Script to filter the output of pdflatex and only print error messages.
"""
from __future__ import print_function
import re
import sys

# regular expression matching an error message from pdflatex. Unfortunately,
# pdflatex only uses stdout, so it is necessary to filter for this.
TEX_ERROR_REGEX = re.compile(".*:[0-9]*:.*")

check_next_line = False
found_error = 0
for line in sys.stdin:
    if check_next_line:
        print(line.rstrip())
        check_next_line = False
        continue

    if TEX_ERROR_REGEX.match(line):
        found_error = 1
        if line.rstrip()[-1] != '.':
            print(line.rstrip(), end="")
            check_next_line = True
        else:
            print(line.rstrip())

if found_error:
    sys.exit(1)
else:
    sys.exit(0)
