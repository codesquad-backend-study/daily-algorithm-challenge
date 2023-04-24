def factorial(number):
    result = 1
    for i in range(1, number + 1):
        result *= i
    return result


n, k = map(int, input().split())
print(factorial(n) // (factorial(k) * factorial(n - k)))
