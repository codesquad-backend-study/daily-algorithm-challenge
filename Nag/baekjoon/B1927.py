import heapq
import sys

input = sys.stdin.readline

# 시간초과 엔딩
# count = int(input().rstrip())
# stack = []
# for _ in range(count):
#     number = int(input().rstrip())
#     if number == 0:
#         print(stack.pop() if stack else 0)
#         continue
#     stack.append(number)
#     stack.sort(reverse=True)

#   Heapq를 쓰면 최소값을 보장하면서 저장한다 개꿀
count = int(input().rstrip())
queue = []
for _ in range(count):
    number = int(input().rstrip())
    if number == 0:
        print(heapq.heappop(queue) if queue else 0)
        continue
    heapq.heappush(queue, number)
