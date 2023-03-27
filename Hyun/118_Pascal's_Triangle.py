class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        d = [[0] * (i + 1) for i in range(numRows)]

        d[0][0] = 1
        for i in range(1, numRows):
            d[i][0] = 1
            d[i][i] = 1                             # 가장자리 처리

            for j in range(1, i):
                d[i][j] = d[i - 1][j - 1] + d[i - 1][j]    # 점화식

        return d


# 파스칼의 삼각형은 가장자리를 제외하면
# d[N][K] = d[N-1][K-1] + d[N-1][K] 점화식을 만족한다.
# 큰 문제를 작은 문제로 쪼개는 점화식을 세우는 것이 DP이다.
