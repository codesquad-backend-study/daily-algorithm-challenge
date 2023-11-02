import math


def solution(n: int) -> int:
    # 숫자니까 반대로 정렬 (어차피 숫자로 인식하니 int()를 해줄 필요 없음)
    nums = sorted(list(str(n)), reverse=True)

    # (number % 30 == 0) == True
    # answer = max(answer, int(tmp))
    # 위 두가지 조건을 기억하면서 풀어 보자

    s_number = ''
    for num in nums:
        s_number += num

    # https://ko.wikipedia.org/wiki/%EB%B0%B0%EC%88%98_%ED%8C%90%EC%A0%95%EB%B2%95
    number = int(s_number)
    if number % 30 == 0:
        return number

    return -1


N = int(input())
print(solution(N))
