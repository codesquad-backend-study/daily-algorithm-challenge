def solution(word):
    alphabets = ['A', 'E', 'I', 'O', 'U']
    answer = []
    order = 0

    def dfs(target):
        nonlocal order
        if target == word:
            answer.append(order)
        if len(target) == 5:
            return

        for alphabet in alphabets:
            order += 1
            dfs(target + alphabet)

    dfs('')
    return answer[0]


solution('I')
