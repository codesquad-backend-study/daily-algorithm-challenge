def solution(N, number):
    if N == number:
        return 1

    results = {1: {N}}

    def calculate(list_A, list_B):
        numbers = set()

        for i in list_A:
            for j in list_B:
                numbers.add(i + j)
                numbers.add(i - j)
                numbers.add(i * j)
                if j != 0:
                    numbers.add(i // j)

        return numbers

    for i in range(2, 9):
        temp = {int(str(N) * i)}

        for j in range(1, i):
            # N의 사용 개수에 중점을 두고 계산한다
            # 예를 들어 N을 4번 사용한 모든 결과가 궁금한 경우, 다음과 같이 계산할 수 있다.
            # N을 1번 사용한 결과 (연산) N을 3번 사용한 결과 = 총 4번 +
            # N을 2번 사용한 결과 (연산) N을 2번 사용한 결과 = 총 4번 +
            # N을 3번 사용한 결과 (연산) N을 1번 사용한 결과 = 총 4번
            temp.update(calculate(results[j], results[i - j]))

            if number in temp:
                return i

        results[i] = temp

    return -1
