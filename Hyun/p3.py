given = [3, 4, 2, -4, -2, -3, 12]
# given = [3, -2, 4, 7, -5, 9, 10, 5, 6, 2, 3, 0]

totals = []
total_dict = {}

totals.append(given[0])
total_dict[given[0]] = 1

for i in range(1, len(given)):                      # 누적합 배열 만들기 + 누적합 맵 만들기
    totals.append(given[i] + totals[i - 1])

    if totals[i] in total_dict:
        total_dict[totals[i]] += 1

    else:
        total_dict[totals[i]] = 1


ans = total_dict[0] if 0 in total_dict else 0       # 초기 배열의 0의 개수


for i in range(len(given)):                         # 누적합 맵에서 value 값 세기 + 누적합 맵에서 value를 하나씩 지우기
    total_dict[totals[i]] -= 1
    ans = max(ans, total_dict[given[i]] if given[i] in total_dict else -1)

    if i == 0:                                  # 첫 번째를 0으로 만드는 경우에만 정답에 1을 추가해준다.
        ans += 1

print(ans)

