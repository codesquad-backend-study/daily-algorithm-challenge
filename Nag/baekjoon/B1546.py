cnt = int(input())
scores = list(map(int, input().split()))
avg = sum(scores) * 100 / (max(scores) * len(scores))
print(avg)
