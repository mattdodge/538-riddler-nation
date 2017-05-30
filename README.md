# 538-riddler-nation

My approach to solving Round 2 of the Battle for Riddler Nation. The goal is to get the most castle points compared to all the other submissions. Read more about the problem at [FiveThirtyEight](http://fivethirtyeight.com/features/the-battle-for-riddler-nation-round-2/).

## TL;DR
Basically, my approach is to generate a lot of random inputs and see which one beats all the rest. The approach to randomizing is a little interesting, read more in the [Randomization](#randomization) section. Ultimately, the solution I went with is this (castle 1, castle 2, ..., castle 10):

```
[0, 5, 5, 5, 13, 8, 2, 32, 22, 8]
```

To (partially) reproduce, run the following to generate 10,000 random submissions and print out the top 10:
```
python generate_random.py 10000 > random1.csv
python winner_check.py random1.csv 10
```

## Scripts in this repo

 * Winner Check Script (`winner_check.py`) - This script takes a list of submissions and figures out the winner. In other words, [Ollie](https://twitter.com/ollie) could have used this script to compute the winner during Round 1.
 * Random Generator Script (`generate_random.py`) - This script generates random solutions. The randomization strategy is described below.
 * Cleanup (`cleanup.py`) - Just does some house keeping on [the data that came from FiveThirtyEight](https://github.com/fivethirtyeight/data/tree/master/riddler-castles).
 
## Randomization

My initial thought was to just pick a random castle for every troop. So, something like this:
```python
for troop in range(100):
    castle[random.randint(1,10)] += 1
```

I quickly realized this was going to give pretty much uniform distributions of troops across all of the castles though, and that would not really mimic the strategies that other submissions would follow (the first submission last time was 100 troops to castle 1 and none anywhere else...) — that would occur 1 in a [Googol](https://en.wikipedia.org/wiki/Googol) times in my algorithm, not good.

Instead, I would rather have bunches of troops at castles, and then some castles with no troops. To make this happen, I choose a random starting castle (1 through 10) and then iterate through the castles (looping back around where necessary). For each castle, choose a random number of troops from 0 to the number of troops remaining. Then put the remaining troops at a random castle. The script is in `generate_random.py` but here is a quick/pseudo-codey version:

```python
troops_remaining = 100
for castle in shift(castles, random.randint(0, 9)):
    troops_for_this_castle = random.randint(0, troops_remaining)
    troops_remaining -= troops_for_this_castle
    castle.add_troops(troops_for_this_castle)
castles[random.randint(0, 9)].add_troops(troops_remaining)
```
