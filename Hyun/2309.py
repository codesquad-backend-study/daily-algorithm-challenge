import itertools
import sys

dwarfs = [int(input()) for _ in range(9)]

dwarfs.sort()
combinations = itertools.combinations(dwarfs, 7)

for combi in combinations:
    if sum(combi) == 100:
        print('\n'.join(map(str, combi)))
        sys.exit(0)
