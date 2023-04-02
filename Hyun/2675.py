t = int(input())

for _ in range(t):

    cnt, word = input().split()
    cnt = int(cnt)

    for ch in word:
        for _ in range(cnt):
            print(ch, end='')
    print()