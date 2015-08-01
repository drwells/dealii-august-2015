#!/usr/bin/env python
"""
Script to filter the output of pdflatex and only warnings and
(optionally) nag results.
"""
from __future__ import print_function
import sys

if "--no-nag" in sys.argv:
    ignore_nag = True
else:
    ignore_nag = False

latex_check_next_line = False
nag_check_next_line = False
for line in sys.stdin:
    if latex_check_next_line:
        print(line.rstrip())
        latex_check_next_line = False
        continue

    if nag_check_next_line:
        print(line.rstrip())
        nag_check_next_line = False
        continue

    if "Label(s) may have changed" in line:
        continue  # we are only compiling once, so ignore this.

    if "LaTeX Warning" in line:
        if line.rstrip()[-1] != '.':
            print(line.rstrip(), end="")
            latex_check_next_line = True
        else:
            print(line.rstrip())
    if not ignore_nag:
        if "nag Warning" in line:
            print(line.rstrip())
        if "(nag)" in line:
            print(line.rstrip(), end="")
            nag_check_next_line = True
