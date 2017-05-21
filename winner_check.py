""" Give it a csv file of solutions, this will spit out the winners

Usage (Load inputs.csv and show the top 10 winners):
    $ python winner_check.py inputs.csv 10
"""

import csv
import sys
from collections import defaultdict

# A list of 10-item lists. One item per solution
inputs = list()

TOP_PLACE = int(sys.argv[2])

with open(sys.argv[1]) as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        inputs.append([int(x) for x in row])

def get_points(soln1, soln2):
    """ Figure out who wins between two solutions

    Returns:
        (soln1Wins, soln1Ties, soln1Losses, soln1Points
         soln2Wins, soln2Ties, soln2Losses, soln2Points)
    """
    soln1Points = soln2Points = 0
    for castle in range(10):
        if soln1[castle] > soln2[castle]:
            soln1Points += (castle + 1)
        elif soln2[castle] > soln1[castle]:
            soln2Points += (castle + 1)
        else:
            soln1Points += (castle + 1) / 2
            soln2Points += (castle + 1) / 2

    return (
        int(soln1Points > soln2Points),
        int(soln1Points == soln2Points),
        int(soln1Points < soln2Points),
        soln1Points,
        int(soln2Points > soln1Points),
        int(soln2Points == soln1Points),
        int(soln2Points < soln1Points),
        soln2Points,
    )

scores = defaultdict(lambda : [0,0,0])
# Run all possible matchups and add up the scores as we go
print("Running {:,} matchups...".format(len(inputs) * (len(inputs) - 1) / 2))
matchup_num = 0
for s1 in range(len(inputs)):
    soln1 = inputs[s1]
    for s2 in range(s1 + 1, len(inputs)):
        soln2 = inputs[s2]
        matchup_num += 1
        if matchup_num % 100000 == 0:
            print("...{:,} complete".format(matchup_num))

        s1W, s1T, s1L, s1P, s2W, s2T, s2L, s2P = get_points(soln1, soln2)

        scores[s1][0] += s1W
        scores[s1][1] += s1T
        scores[s1][2] += s1L
        scores[s2][0] += s2W
        scores[s2][1] += s2T
        scores[s2][2] += s2L

sorted_scores = sorted(scores.items(),
                       key=lambda (num, score) : score[0] + 0.5 * score[1],
                       reverse=True)

for place in range(TOP_PLACE):
    print("Place #{} : {}".format(place+1, sorted_scores[place]))
    print(inputs[sorted_scores[place][0]])
    print("")
