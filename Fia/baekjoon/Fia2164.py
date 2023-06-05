# 카드 2
import collections

N = int(input())

deque = collections.deque(number for number in range(1, N + 1))

while len(deque) > 1:
    deque.popleft()
    deque.append(deque.popleft())

print(deque[0])
