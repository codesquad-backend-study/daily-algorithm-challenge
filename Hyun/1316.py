def check_not_group(s: str):
    word = {}
    prev = s[0]
    word[prev] = 1

    for ch in s[1:]:
        if prev != ch:
            if ch in word:
                return 1
            word[ch] = 1
        prev = ch

    return 0

t = int(input())

ans = t
for _ in range(t):
    ans -= check_not_group(input())

print(ans)