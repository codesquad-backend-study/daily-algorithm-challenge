# 카드 정렬하기
import heapq
import sys

N = int(sys.stdin.readline())
heap = []
for _ in range(N):
    heapq.heappush(heap, int(sys.stdin.readline()))

count = 0
while len(heap) > 1:
    sum_of_min = heapq.heappop(heap) + heapq.heappop(heap)  # 작은 카드 묶음끼리 먼저 더하기
    heapq.heappush(heap, sum_of_min)  # 더한 값을 다시 집어 넣기
    count += sum_of_min

print(count)

