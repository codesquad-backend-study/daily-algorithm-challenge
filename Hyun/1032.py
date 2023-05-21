texts = []
for _ in range(int(input())):
    texts.append(input())

ans = ''

for idx in range(len(texts[0])):
    check = set()
    for text in texts:
        check.add(text[idx])

    ans += check.pop() if len(check) == 1 else "?"

print(ans)


