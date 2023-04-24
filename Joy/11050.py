import sys

n, k = map(int, sys.stdin.readline().split())

def  factorial(n) :
    answer = 1
    for i in range(2, n+1) :
        answer *= i
    return answer
mo = factorial(n)
ja = factorial(n-k) * factorial(k)

print(mo//ja)