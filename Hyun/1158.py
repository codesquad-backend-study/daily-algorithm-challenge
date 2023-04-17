people_cnt, interval = map(int, input().split())

people = [i for i in range(1, people_cnt+1)]
ans = []

idx = 0
while people:
    idx = (idx + interval - 1) % len(people)
    ans.append(people[idx])
    people.pop(idx)

print("<", end="")
print(*ans, sep=", ", end="")
print(">")