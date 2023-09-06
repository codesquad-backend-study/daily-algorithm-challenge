import sys

for _ in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    numbers = []
    for _ in range(n):
        numbers.append(sys.stdin.readline().rstrip())

    numbers.sort()

    result = "YES"
    for i in range(len(numbers)-1):
        if numbers[i+1].startswith(numbers[i]):
            result = "NO"
            break
    print(result)
