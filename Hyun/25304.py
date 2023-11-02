total = int(input())
n = int(input())

summation = 0
for _ in range(n):
    each, cnt = map(int, input().split())
    summation += each * cnt

print('Yes' if total == summation else 'No')
