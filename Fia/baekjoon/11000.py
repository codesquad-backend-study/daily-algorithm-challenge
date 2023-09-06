# 강의실 배정
import heapq
import sys

# 시간 초과 실패
# N = int(sys.stdin.readline())
# heap = []
#
# for _ in range(N):
#     start, end = map(int, sys.stdin.readline().split())
#     lecture = (start, end)
#     heapq.heappush(heap, lecture)
#
# ends = [0]
# while heap:
#     start, end = heapq.heappop(heap)
#
#     updated = False
#     for index, current_end in enumerate(ends):
#         if start >= current_end:
#             ends[index] = end
#             updated = True
#             break
#
#     if not updated:
#         ends.append(end)
#
# print(len(ends))

N = int(sys.stdin.readline())
lectures = []

for _ in range(N):
    start, end = map(int, sys.stdin.readline().split())
    lecture = (start, end)
    lectures.append(lecture)

lectures.sort()

ends = []
heapq.heappush(ends, lectures[0][1])
for i in range(1, N):
    if lectures[i][0] < ends[0]:
        heapq.heappush(ends, lectures[i][1])
    else:
        heapq.heappop(ends)
        heapq.heappush(ends, lectures[i][1])

print(len(ends))
