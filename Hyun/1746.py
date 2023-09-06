n, m = map(int, input().split())
dont_listened = {input(): 1 for _ in range(n)}

ans = []

for _ in range(m):
    dont_seen = input()
    if dont_seen in dont_listened:
        ans.append(dont_seen)

print(len(ans))
ans.sort()
print('\n'.join(ans))

