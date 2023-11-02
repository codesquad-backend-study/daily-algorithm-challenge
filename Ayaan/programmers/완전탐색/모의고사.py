def solution(answers):
    supo1 = [1, 2, 3, 4, 5]
    supo2 = [2, 1, 2, 3, 2, 4, 2, 5]
    supo3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    answer_cnt = [0, 0, 0]

    for i, answer in enumerate(answers):
        if supo1[i % len(supo1)] == answer:
            answer_cnt[0] += 1
        if supo2[i % len(supo2)] == answer:
            answer_cnt[1] += 1
        if supo3[i % len(supo3)] == answer:
            answer_cnt[2] += 1

    max_cnt = max(answer_cnt)
    result = []
    for i, cnt in enumerate(answer_cnt):
        if cnt == max_cnt:
            result.append(i + 1)

    return result


solution([1, 3, 2, 4, 2])
