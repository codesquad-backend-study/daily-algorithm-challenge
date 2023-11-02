def solution(A, I):
    # 어떻게 올림하기 전을 추측할까를 계속 고민해 보았는데
    # "적어도 몇 곡"이 있는지를 묻는 문제였음
    # 이건 그냥 완전 수학문제네

    # (melody / A = I) -> (melody = I * A)
    # 평균에서 일단 1을 빼준 이후에 나중에 1 더해주기
    # 그럼 오차 수정됨
    melody = (I - 1) * A + 1
    return melody


# 앨범에 수록된 곡의 개수 A, 평균값 I
A, I = map(int, input().split())
print(solution(A, I))
