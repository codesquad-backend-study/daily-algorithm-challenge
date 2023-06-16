# 회전하는 큐
import collections

N, M = map(int, input().split())
deque = collections.deque(number for number in range(1, N + 1))

numbers = collections.deque(map(int, input().split()))
count = 0

while numbers:
    target = numbers[0]
    first = deque[0]

    if target != first:
        left = deque.index(target)
        right = len(deque) - left
        if left >= right:
            while target != first:
                deque.appendleft(deque.pop())
                first = deque[0]
                count += 1
        else:
            while target != first:
                deque.append(deque.popleft())
                first = deque[0]
                count += 1

    numbers.popleft()
    deque.popleft()

print(count)
