def solution(numbers):
    #     def eratos():
    #         MAX = 9999999 + 1

    #         prime = [True] * MAX
    #         prime[0] = prime[1] = False

    #         for i in range(2, MAX//2 + 1):
    #             if prime[i]:
    #                 for j in range(i+i, MAX, i):
    #                     prime[j] = False

    #         return prime          # 에라토스테네스의 체 쓰면 느림 ㅋ

    def is_prime(num):
        if num < 2:
            return False

        for i in range(2, int(num ** (1 / 2)) + 1):
            if num % i == 0:
                return False

        return True

    def permutation(arr: list, pick_cnt):
        used = [False] * len(arr)

        def generate(picks):
            if len(picks) == pick_cnt:
                num = int(''.join(map(str, picks)))
                if is_prime(num):
                    ans.add(num)
                return

            for i in range(len(arr)):
                if not used[i]:
                    picks.append(arr[i])
                    used[i] = True
                    generate(picks)
                    used[i] = False
                    picks.pop()

        generate([])

    numbers = list(map(int, list(numbers)))
    ans = set()

    for i in range(1, len(numbers) + 1):
        permutation(numbers, i)

    return len(ans)
