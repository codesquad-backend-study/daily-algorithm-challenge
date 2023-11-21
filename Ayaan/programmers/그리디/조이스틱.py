def solution(name):
    def cal_cnt(ch):
        if ord(ch) - ord('A') > 13:
            return ord('Z') - ord(ch) + 1
        else:
            return ord(ch) - ord('A')

    answer = 0
    move = len(name) - 1
    for i, alpha in enumerate(name):
        answer += cal_cnt(alpha)

        A_idx = i + 1
        while A_idx < len(name) and name[A_idx] == 'A':
            A_idx += 1

        # 앞으로 가다가 A를 만나면 뒤로 돌아가는 경우
        move = min(move, 2 * i + (len(name) - A_idx))
        # 처음부터 뒤로 돌아갔다가 다시 앞으로 오는 경우
        move = min(move, 2 * (len(name) - A_idx) + i)

    return answer + move


solution('JEROEN')
