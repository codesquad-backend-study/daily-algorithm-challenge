import itertools
import math


def solution(numbers):
    def isPrime(num):
        if num < 2:
            return False
        for i in range(2, int(math.sqrt(num) + 1)):
            if num % i == 0:
                return False
        return True

    answer = set()
    numbers = list(numbers)

    for i in range(1, len(numbers) + 1):
        combinations = itertools.permutations(numbers, i)
        for combi in combinations:
            number = int(''.join(combi))
            if isPrime(number):
                answer.add(number)

    return len(answer)


solution('011')
