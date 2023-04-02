def solution():
    N = int(input())
    for i in range(N):
        score = 0
        total = 0
        result = input()
        for ox in result:
            if ox == 'O':
                score += 1
                total += score
            else:
                score = 0
        print(total)

solution()