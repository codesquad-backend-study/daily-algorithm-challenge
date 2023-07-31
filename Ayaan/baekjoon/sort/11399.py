N = int(input())
time_list = list(map(int, input().split()))
time_list.sort()

waiting = 0
sum = 0
for time in time_list:
    time = int(time)
    sum += (waiting + time)
    waiting += time
print(sum)
