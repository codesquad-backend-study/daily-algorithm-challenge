# 베스트셀러
import collections
import sys

N = int(sys.stdin.readline())

sold = sorted([sys.stdin.readline().strip() for _ in range(N)])

counter = collections.Counter(sold)
print(counter.most_common(1)[0][0])
