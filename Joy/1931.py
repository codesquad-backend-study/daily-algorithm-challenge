import sys

n = int(input())

meeting = []
for i in range(n) :
    tmp = tuple(map(int, sys.stdin.readline().split()))
    meeting.append(tmp)

meeting.sort()

# 앞 1번째와 뒤 0번째 비교 -> 전자가 더 크면 둘의 1번째 요소 비교해 더 작은걸 살림. 인덱스 교체.
#                     -> 후자가 더 크면 둘다 살림. 인덱스 뒤걸로 교체.

idx = 0
for i in range(1,n) :
    end = meeting[idx][1]
    start = meeting[i][0]
    end2 = meeting[i][1]
    if end > start :
        if end > end2 :
            meeting[idx] = False
            idx = i
        else :
            meeting[i] = False
    else :
        idx = i
print(n-meeting.count(False))
