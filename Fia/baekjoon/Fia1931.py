# 회의실 배정
# 겹치지 않는 회의의 최대 수 찾기
# 같은 시간에 시작하면 빨리 끝나는 회의가 좋다
import sys

count = int(sys.stdin.readline())
all_meetings = []  # 시작 시간, 종료 시간

for _ in range(count):
    meeting = sys.stdin.readline().split()
    start_time = int(meeting[0])
    end_time = int(meeting[1])

    all_meetings.append([start_time, end_time])

all_meetings.sort(key=lambda time: (time[0], time[1]))  # 이른 시작 시간, 빠른 종료 시간 순서로 정렬한다

result = 1
current_end_time = 10000000

for meeting in all_meetings:
    start = meeting[0]
    end = meeting[1]
    if end < current_end_time:  # 현재 회의 종료 시간보다 더 일찍 끝나는 회의라면
        current_end_time = end  # 해당 회의의 종료 시간을 현재 종료 시간으로 수정하여 계속 탐색한다
        continue
    if start >= current_end_time:  # 현재 종료된 회의 이후의 회의라면
        current_end_time = end  # 해당 회의의 종료 시간을 현재 종료 시간으로 수정하고
        result += 1  # 회의실 사용이 가능하기 때문에 개수를 1 증가시킨다

print(result)
