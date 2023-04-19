def solution():
    day = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]
    x, y = map(int, input().split())
    
    date = 0
    for i in range(1, x):
        if i==4 or i==6 or i==9 or i==11:
            date += 30
        elif i==2:
            date += 28
        else:
            date += 31
    date += y
    
    print(day[date % 7 - 1])
    
solution()