import math
from itertools import permutations


def solution(numbers):
    def isPrime(number):
        check = [False] * (int(math.sqrt(number)) + 1)

        for i in range(2, len(check)):
            if not check[i]:
                if number % i != 0:
                    for j in range(i, len(check), i):
                        check[j] = True
                else:
                    return False

        return True

    groups = set()

    for length in range(1, len(numbers) + 1):
        for group in permutations(numbers, length):
            groups.add(int(''.join(list(group))))

    count = 0

    for number in groups:
        if number > 1 and isPrime(number):
            count += 1

    return count
