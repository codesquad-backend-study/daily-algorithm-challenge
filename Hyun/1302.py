import collections

n = int(input())

books = [input() for _ in range(n)]

counter = collections.Counter(books)

l = sorted(counter.most_common(), key=lambda x: (-x[1], x[0]))
print(l[0][0])
