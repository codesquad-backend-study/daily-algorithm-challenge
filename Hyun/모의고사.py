def solution(answers):
    pick_1 = [1, 2, 3, 4, 5]
    pick_2 = [2, 1, 2, 3, 2, 4, 2, 5]
    pick_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    score = [0, 0, 0]

    for idx, each in enumerate(answers):
        score[0] += each == pick_1[idx % len(pick_1)]
        score[1] += each == pick_2[idx % len(pick_2)]
        score[2] += each == pick_3[idx % len(pick_3)]

    max_score = max(score)

    ans = []
    for idx, score in enumerate(score, 1):
        if score == max_score:
            ans.append(idx)

    return ans
