def solution(numbers):
    ans = ''.join(sorted([str(number) for number in numbers], reverse=True, key=lambda x: x * 3))

    return str(int(ans))
