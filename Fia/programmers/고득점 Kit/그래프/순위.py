def solution(n, results):
    points = [[0] * (n + 1) for _ in range(n + 1)]

    # points[1][2] = 1 : 1번 선수가 2번 선수에게 승
    # points[2][1] = -1 : 2번 선수가 1번 선수에게 패
    for win, lose in results:
        points[win][lose] = 1;
        points[lose][win] = -1;

    # k : 거쳐가는 선수
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                # k 선수를 거쳐서 비교했을 때, i가 k를 이기고 k가 j를 이기면 i가 j를 이김
                if points[i][k] == 1 and points[k][j] == 1:
                    points[i][j] = 1
                    points[j][i] = -1
                # k 선수를 거쳐서 비교했을 때, i가 k에게 지고 k가 j에게 지면 j가 i를 이김
                elif points[i][k] == -1 and points[k][j] == -1:
                    points[i][j] = -1
                    points[j][i] = 1

    answer = 0
    for i in range(1, n + 1):
        count = 0

        # 자기 자신을 제외한 선수와의 결과가 0이 아니면 승부를 알 수 있음
        for j in range(1, n + 1):
            if points[i][j] == 0:
                count += 1

        if count == 1:
            answer += 1

    return answer
