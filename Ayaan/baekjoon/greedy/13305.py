N = int(input())
distances = [*map(int, input().split())]
prices = [*map(int, input().split())]

result = 0
distance = 0
current = prices[0]
for i in range(len(prices) - 1):
    # 현재 도시의 가격이 이전 보다 작으면 갱신
    if prices[i] < current:
        current = prices[i]

    distance += distances[i]
    # 다음 도시의 가격이 현재 보다 작으면 주유
    if current > prices[i + 1]:
        result += current * distance
        distance = 0

# 마지막 도시의 가격이 커서 주유를 안한 경우
if distance > 0:
    result += current * distance

print(result)
