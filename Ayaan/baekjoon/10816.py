import collections

card_count = collections.defaultdict(int)
N = input()
for num in input().split():
    card_count[num] += 1

M = input()
for num in input().split():
    print(card_count[num], end=" ")
