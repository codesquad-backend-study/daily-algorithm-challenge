# 30

import sys

street_number = sys.stdin.readline().strip()

if '0' not in street_number or sum(map(int, street_number)) % 3 != 0:
    print(-1)
else:
    print(''.join(sorted(street_number, reverse=True)))
