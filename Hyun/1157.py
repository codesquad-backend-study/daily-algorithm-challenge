import collections

s = input().upper()
if len(s) == 1:
    print(s)
else:
    counter = collections.Counter(s).most_common(2)
    first, second = counter[0][0], counter[1][0]
    print(first if counter[0][1] > counter[1][1] else '?')

