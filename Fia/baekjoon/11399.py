# ATM

number_of_people = int(input())
times = sorted([time for time in map(int, input().split())])

total_time = 0
waiting_time = 0
for time in times:
    total_time += waiting_time + time
    waiting_time += time

print(total_time)
