def solution(money):
    # 전 집에서 훔쳤을 경우 : 이번 집에서 훔칠 수 없음
    # 전 집에서 훔치지 않았을 경우 : 이번 집에서 훔칠 수 있음

    # 첫 번째 집에서 시작하는 경우 + 두 번째 집에서 시작하는 경우
    # [전 집에서 훔친 경우, 전 집에서 훔치지 않은 경우, 전 집에서 훔친 경우, 전 집에서 훔치지 않은 경우]
    results = [[0, 0, 0, 0] for _ in range(len(money))]

    results[0][0] = money[0]

    for i in range(1, len(money)):
        results[i][0] = results[i - 1][1] + money[i]  # 이번 집에서 훔침
        results[i][1] = max(results[i - 1][0], results[i - 1][1])  # 이번 집에서 훔치지 않음
        results[i][2] = results[i - 1][3] + money[i]  # 이번 집에서 훔침
        results[i][3] = max(results[i - 1][2], results[i - 1][3])  # 이번 집에서 훔치지 않음

    return max(results[-1][1], results[-1][2], results[-1][3])
