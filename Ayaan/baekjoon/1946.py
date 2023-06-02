for _ in range(int(input())):
    N = int(input())
    scores = []
    for _ in range(N):
        scores.append(list(map(int, input().split())))
    scores.sort(key=lambda x: x[0])
    # 서류점수로 정렬하고 면접점수만 비교한다.
    count = 1
    min_score = scores[0][1]
    # 앞에 있는 면접점수 최솟값 보다 작으면 합격
    for i in range(1, len(scores)):
        score = scores[i][1]
        if score < min_score:
            count += 1
        min_score = min(min_score, score)
        # 앞에서 1등이 나왔으면 뒤에는 모두 불합격
        if min_score == 1:
            break
    print(count)
