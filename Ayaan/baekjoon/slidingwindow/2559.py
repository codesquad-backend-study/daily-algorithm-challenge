N, K = map(int, input().split())
temperatures = [*map(int, input().split())]

sum_temperature = sum(temperatures[:K])
answer = sum_temperature

for i in range(1, N - K + 1):
    sum_temperature -= temperatures[i - 1]
    sum_temperature += temperatures[i + K - 1]
    answer = max(answer, sum_temperature)
print(answer)
