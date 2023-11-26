from typing import List


def solution(n: int, lost: List[int], reserve: List[int]) -> int:
    # 각 배열의 고유의 학생 만들기
    lost_only = list(set(lost) - set(reserve))
    reserve_only = list(set(reserve) - set(lost))

    # 고유의 현재 reserve의 학생의 앞과 뒤를 확인하여 빌려주기
    for current_reserve in reserve_only:
        # 왜 "- 1"이 front냐고 생각할 수 있는데,
        # [1, 2, 3]번 학생이 있고, 현재가 2라고 치면 당연히 앞에 있는 학생은 1이겠지
        front = current_reserve - 1
        back = current_reserve + 1

        if front in lost_only:
            lost_only.remove(front)
            continue

        if back in lost_only:
            lost_only.remove(back)

    return n - len(lost_only)


print(solution(5, [2, 4], [1, 3, 5]))
print(solution(5, [2, 4], [3]))
print(solution(3, [3], [1]))
