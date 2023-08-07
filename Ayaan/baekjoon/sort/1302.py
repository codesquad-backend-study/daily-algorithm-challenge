import collections

N = int(input())
book_count = collections.defaultdict(int)
for _ in range(N):
    book_count[input()] += 1

book_count = sorted(book_count.items())
print(max(book_count, key=lambda x: x[1])[0])
