# 0 ~ 2 : 3sec -> //3 + 3
# 3 ~ 5 : 4sec
# 6 ~ 8
# 9 ~ 11
# 12 ~ 14          //3 + 3 -> 7sec

# 15 ~ 18 , (4개)
# 19 ~ 21
# 22 ~ 25, (4개)

offset_to_sec = {15: 8, 16: 8, 17: 8, 18: 8, 19: 9, 20: 9, 21: 9, 22: 10, 23: 10, 24: 10, 25: 10}

s = input()
total_sec = 0
for ch in s:
    offset = ord(ch) - ord('A')

    if offset < 15:
        total_sec += offset // 3 + 3
    else:
        total_sec += offset_to_sec[offset]

print(total_sec)

