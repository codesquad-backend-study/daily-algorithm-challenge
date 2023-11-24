from collections import deque


def solution(numbers, target):
    count = 0

    queue = deque([[numbers[0], 0], [-numbers[0], 0]])

    while queue:
        number, index = queue.popleft()

        if index == len(numbers) - 1:
            if number == target:
                count += 1
            continue

        queue.append([number + numbers[index + 1], index + 1])
        queue.append([number - numbers[index + 1], index + 1])

    return count
