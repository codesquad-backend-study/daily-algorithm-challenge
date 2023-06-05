t = int(input())
for _ in range(t):
    n = int(input())
    members = []

    for _ in range(n):
        members.append(tuple(map(int, input().split())))

    members.sort(key=lambda x: x[0])

    best_ranking = 1000000
    hire_count = 0
    for _, rank in members:
        if best_ranking > rank:
            hire_count += 1
            best_ranking = rank

    print(hire_count)
