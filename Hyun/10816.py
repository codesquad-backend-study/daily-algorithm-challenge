import collections

numbers = collections.defaultdict(int)

input()
given = list(map(int, input().split()))

for each in given:
    numbers[each] += 1

input()
find = list(map(int, input().split()))

for each in find:
    print(numbers[each], end=" ")
