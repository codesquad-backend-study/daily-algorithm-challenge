s = input()

ans = [-1] * 26

for i in range(len(s) - 1, -1, -1):
    ans[ord(s[i]) - ord('a')] = i

print(*ans)
