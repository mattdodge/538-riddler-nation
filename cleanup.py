""" Clean up the Round 1 solutions.

Basically, remove the explanations.

Run like so:
$ python cleanup.py round-1-solns.csv > round-1-solns-cleaned.csv
"""

import csv
import sys

with open(sys.argv[1]) as csvfile:
    csvfile.next() # skip first line
    reader = csv.reader(csvfile)
    for row in reader:
        print(','.join(row[:-1]))
