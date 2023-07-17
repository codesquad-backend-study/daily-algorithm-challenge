# 트리
import collections
import sys

N = int(sys.stdin.readline())
parents = list(map(int, sys.stdin.readline().strip().split()))
number_to_remove = int(sys.stdin.readline())

if N == 1:
    print(0)
    exit()

trees = collections.defaultdict(list)

for index, parent in enumerate(parents):
    trees[parent].append(index)

if number_to_remove == trees[-1][0]:
    print(0)
    exit()

queue = collections.deque(trees[-1])
count = 0

while queue:
    node = queue.popleft()

    if len(trees[node]) == 0:
        count += 1
        continue

    check = 0
    for child in trees[node]:
        if child == number_to_remove:
            check += 1
            continue
        queue.append(child)

    if check == len(trees[node]):
        count += 1

print(count)
