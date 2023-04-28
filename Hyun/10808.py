ans = [0] * 26

s = input()

for ch in s:
    ans[ord(ch) - ord('a')] += 1

print(*ans) 
