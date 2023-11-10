def solution(brown, yellow):
    total = brown + yellow

    for i in range(1, total + 1):
        j = total // i

        if i * j == total:
            width = max([i, j])
            height = min([i, j])

            current_yellow = (width - 2) * (height - 2)
            current_brown = width * height - current_yellow

            if current_yellow == yellow and current_brown == brown:
                return [width, height]

# 테스트 1 〉	통과 (0.01ms, 10.1MB)
# 테스트 2 〉	통과 (0.01ms, 10.2MB)
# 테스트 3 〉	통과 (0.15ms, 10.1MB)
# 테스트 4 〉	통과 (0.01ms, 10.2MB)
# 테스트 5 〉	통과 (0.01ms, 10.1MB)
# 테스트 6 〉	통과 (0.05ms, 10.4MB)
# 테스트 7 〉	통과 (0.08ms, 10.2MB)
# 테스트 8 〉	통과 (0.09ms, 10.2MB)
# 테스트 9 〉	통과 (0.16ms, 10MB)
# 테스트 10 〉	통과 (0.11ms, 10.2MB)
# 테스트 11 〉	통과 (0.01ms, 10.1MB)
# 테스트 12 〉	통과 (0.01ms, 10.1MB)
# 테스트 13 〉	통과 (0.01ms, 10.2MB)
