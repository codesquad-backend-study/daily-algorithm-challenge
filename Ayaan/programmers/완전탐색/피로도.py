import itertools


def solution(k, dungeons):
    answer = -1

    permutations = itertools.permutations(dungeons, len(dungeons))
    for permutation in permutations:
        cnt = 0
        hp = k
        for dungeon in permutation:
            if hp >= dungeon[0]:
                hp -= dungeon[1]
                cnt += 1
            else:
                break
        answer = max(answer, cnt)

    return answer


solution(80, [[80, 20], [50, 40], [30, 10]])
