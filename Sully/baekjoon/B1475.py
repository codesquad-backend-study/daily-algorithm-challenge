def solution(N):
    S = str(N)
    # 딕셔너리 생성
    dic = make_dic()
    # 메인 로직
    for s in S:
        if s == '6' or s == '9':
            # 6, 9는 같은 걸로 보자
            check69(dic)
            continue

        dic[int(s)] += 1
    return max(dic.values())


def check69(dic):
    if dic[6] == dic[9]:
        dic[6] += 1
        return

    dic[9] += 1


def make_dic():
    # 1세트 -> 0 ~ 9
    return {key: 0 for key in range(10)}


print(solution(int(input())))
