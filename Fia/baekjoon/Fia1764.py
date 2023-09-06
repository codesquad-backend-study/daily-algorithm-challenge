import sys

N, M = map(int, sys.stdin.readline().split())

unheard = {}
for _ in range(N):
    people = sys.stdin.readline().strip()
    unheard[people] = True

result = []
for _ in range(M):
    people = sys.stdin.readline().strip()
    if unheard.get(people) is not None:
        result.append(people)

result.sort()

print(len(result))
print(*result, sep="\n")
