import heapq

n = int(input())

numbers = [-1000000001] * n

for _ in range(n):
    for num in list(map(int, input().split())):
        if numbers[0] <= num:
            heapq.heappop(numbers)
            heapq.heappush(numbers, num)

print(heapq.heappop(numbers))
