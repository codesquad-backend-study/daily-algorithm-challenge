import collections


def solution(people, limit):
    people.sort()
    queue = collections.deque(people)

    count = 0
    while queue:
        fat = queue.pop()
        if queue and queue[0] + fat <= limit:
            queue.popleft()

        count += 1

    return count
