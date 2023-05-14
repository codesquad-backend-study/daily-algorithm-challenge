count = []
people = 0

for _ in range(4):
    get_off, get_on = map(int, input().split())
    people = people - get_off + get_on
    count.append(people)

print(max(count))
