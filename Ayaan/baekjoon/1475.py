num_count = {i:0 for i in range(10)}
room_number = input()

for num in room_number:
    num_count[int(num)] += 1

six_plus_nine = num_count[6] + num_count[9]
# 6+9의 개수를 2로 나눈다.
# 6+9의 개수가 홀수이면 2로 나누고 1을 더해준다.
num_count[6] = six_plus_nine // 2 if six_plus_nine % 2 == 0 else six_plus_nine // 2 + 1
num_count[9] = 0

print(max(num_count.values()))