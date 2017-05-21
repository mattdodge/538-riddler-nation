""" Generate some random strategies

Usage (generate 100 random strategies):
    python generate_random.py 100 > strategies.csv
"""
import sys
import random

NUM_TO_GENERATE = int(sys.argv[1])


for i in range(NUM_TO_GENERATE):
    num_troops_remaining = 100
    castles = [0] * 10
    starting_castle = random.randint(0, 9)

    for castle_num in range(10):
        actual_castle_num = (castle_num + starting_castle) % 10
        this_castle = random.randint(0, num_troops_remaining)
        castles[actual_castle_num] = this_castle
        num_troops_remaining -= this_castle

    print(",".join([str(c) for c in castles]))
