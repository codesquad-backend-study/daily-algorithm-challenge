calendar = {month: 31 for month in range(1, 13)}

for month in [4, 6, 9, 11]:
    calendar[month] -= 1

calendar[2] = 28  # 달력설정

day_of_the_week = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]

month, date = map(int, input().split())

day_diff = 0

for i in range(1, month):  # 1월부터 전월까지
    day_diff += calendar[i]
day_diff += date

print(day_of_the_week[day_diff % 7])
