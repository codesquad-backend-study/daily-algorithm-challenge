def solution(k, dungeons):
    def permutations(arr, n):
        visit = [False] * len(arr)
        perms = []

        def generate(pick):
            if len(pick) == n:
                perms.append(pick[:])
                return

            for i in range(len(arr)):
                if not visit[i]:
                    visit[i] = True
                    pick.append(arr[i])
                    generate(pick)
                    visit[i] = False
                    pick.pop()

        generate([])

        return perms

    cases = permutations(dungeons, len(dungeons))

    ans = 0
    for case in cases:
        current_fatigue = k
        count = 0
        for need_fatigue, consume_fatigue in case:
            if current_fatigue < need_fatigue:
                break
            count += 1
            current_fatigue -= consume_fatigue
        ans = max(count, ans)

    return ans
