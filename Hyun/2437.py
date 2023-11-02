n = int(input())
numbers = sorted(list(map(int, input().split())))

summ = 1                 # 시작이 1이 아닐 수 있기 때문에 1부터 시작

for num in numbers:
    if summ < num:          # 누적합 + 1 < numbers[i] 인 경우 누적합 + 1 을 잴 수 없다.
        break

    summ += num

print(summ)         # 시작 때 1 더해줬기 때문에 누적합 + 1 = summ 이다.
