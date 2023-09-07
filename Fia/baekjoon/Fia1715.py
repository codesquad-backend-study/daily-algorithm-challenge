# 카드 정렬하기
import heapq
import sys

count = int(sys.stdin.readline())
cards = [int(sys.stdin.readline()) for _ in range(count)]

heapq.heapify(cards)

answer = 0

while len(cards) > 1:
    dummy = heapq.heappop(cards) + heapq.heappop(cards)
    answer += dummy
    heapq.heappush(cards, dummy)

print(answer)



