# 쉬운 계단 수

length = int(input())

# 길이가 2인 경우 [길이 0, 길이 1, 길이 2] 이렇게 총 3개의 배열을 만든다
accumulated_count = [[0] * 10 for _ in range(length + 1)]
# 길이가 1인 경우 0을 제외한 각 숫자로 끝나는 경우의 수는 모두 1개이다 [0으로 끝나는 경우의 수, 1로 끝나는 경우의 수, 2로 끝나는 경우의 수 ...]
accumulated_count[1] = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]

for i in range(2, length + 1):
    for j in range(10):
        if j == 0:
            # 맨 뒤의 숫자가 1인 경우에만 맨 뒤의 숫자가 0인 수를 만들 수 있다
            accumulated_count[i][j] = accumulated_count[i - 1][1]
        elif 1 <= j <= 8:
            # 자신의 앞 또는 뒤의 숫자가 자신이 맨 뒤의 숫자인 수를 만들 수 있다
            accumulated_count[i][j] = accumulated_count[i - 1][j - 1] + accumulated_count[i - 1][j + 1]
        else:
            # 맨 뒤의 숫자가 8인 경우에만 맨 두의 숫자가 9인 수를 만들 수 있다
            accumulated_count[i][j] = accumulated_count[i - 1][8]

print(sum(accumulated_count[-1]) % 1_000_000_000)
