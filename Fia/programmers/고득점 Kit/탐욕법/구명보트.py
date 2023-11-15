def solution(people, limit):
    people.sort(reverse=True)

    front = 0
    back = len(people) - 1
    boat = 0

    while front <= back:
        if people[front] + people[back] <= limit:
            back -= 1

        front += 1
        boat += 1

    return boat
