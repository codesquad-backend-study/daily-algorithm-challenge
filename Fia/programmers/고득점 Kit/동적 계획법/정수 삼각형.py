def solution(triangle):
    if len(triangle) == 1:
        return triangle[0][0]

    results = []
    for i in range(len(triangle)):
        results.append([0] * len(triangle[i]))

    results[0] = [triangle[0][0]]

    for i in range(len(triangle) - 1):
        for j in range(len(triangle[i])):
            results[i + 1][j] = max(results[i][j] + triangle[i + 1][j], results[i + 1][j])
            results[i + 1][j + 1] = max(results[i][j] + triangle[i + 1][j + 1], results[i + 1][j + 1])

    print(results)

# 테스트 1 〉	통과 (0.03ms, 10MB)
# 테스트 2 〉	통과 (0.08ms, 10.1MB)
# 테스트 3 〉	통과 (0.10ms, 10.2MB)
# 테스트 4 〉	통과 (0.59ms, 10.2MB)
# 테스트 5 〉	통과 (2.46ms, 10.4MB)
# 테스트 6 〉	통과 (0.68ms, 10.1MB)
# 테스트 7 〉	통과 (3.80ms, 10.3MB)
# 테스트 8 〉	통과 (0.53ms, 10.3MB)
# 테스트 9 〉	통과 (0.02ms, 10.2MB)
# 테스트 10 〉	통과 (0.34ms, 10.1MB)
# 효율성  테스트
# 테스트 1 〉	통과 (90.96ms, 17.8MB)
# 테스트 2 〉	통과 (61.80ms, 16MB)
# 테스트 3 〉	통과 (89.36ms, 18.9MB)
# 테스트 4 〉	통과 (89.09ms, 17.9MB)
# 테스트 5 〉	통과 (83.65ms, 17.2MB)
# 테스트 6 〉	통과 (104.07ms, 19.1MB)
# 테스트 7 〉	통과 (86.51ms, 18.6MB)
# 테스트 8 〉	통과 (70.43ms, 17MB)
# 테스트 9 〉	통과 (75.51ms, 17.4MB)
# 테스트 10 〉	통과 (88.77ms, 18.5MB)
