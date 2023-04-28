import math

number = int(input())
dic = {key: 0 for key in range(0, 9)}
while number != 0:
    key = number % 10
    number = number // 10
    if key == 9:
        dic[6] += 1
        continue
    dic[key] += 1
dic[6] = math.ceil(dic[6] / 2)
print(max(dic.values()))
