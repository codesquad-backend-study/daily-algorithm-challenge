N, M = map(int, input().split())

not_hear = {}
for _ in range(N):
    not_hear[input()] = 1

not_hear_not_see = []
for _ in range(M):
    name = input()
    if name in not_hear:
        not_hear_not_see.append(name)

not_hear_not_see.sort()
print(len(not_hear_not_see))
print(*not_hear_not_see, sep="\n")
