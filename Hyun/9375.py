import collections

t = int(input())

for _ in range(t):
    n = int(input())
    closet = collections.defaultdict(list)

    for _ in range(n):
        cloth, kind = input().split()
        closet[kind].append(cloth)

    ans = 1
    for _, clothes in closet.items():
        ans *= (len(clothes) + 1)

    print(ans - 1)
