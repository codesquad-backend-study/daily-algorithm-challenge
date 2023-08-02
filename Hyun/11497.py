t = int(input())

for _ in range(t):
    n = int(input())
    numbers = list(map(int, input().split()))

    odd = []
    even = []
    for idx, number in enumerate(sorted(numbers)):
        if idx % 2 == 0:
            even.append(number)
        else:
            odd.append(number)

    numbers = odd + even[::-1]

    ans = 0
    prev = numbers[0]
    for number in numbers:
        ans = max(ans, abs(prev - number))
        prev = number

    print(ans)
