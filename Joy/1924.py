import sys

month, day = map(int, sys.stdin.readline().split())

calendar = { 1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31 }

date = { 0:'SUN' ,1:'MON', 2:'TUE', 3:'WED', 4:'THU', 5:'FRI', 6:'SAT' }

while month > 1:
    month += -1
    day += calendar[month]

print(date[day%7])