n = int(input())
numbers = list(map(int, input().split()))

total = 0
wait_time = 0

for each in sorted(numbers):
    total += wait_time + each
    wait_time += each

print(total)
