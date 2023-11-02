class Solution:
    def climbStairs(self, n: int) -> int:
        # 피보나치 수열 문제입니다.(an = an_1 + an_2
        # 수학의 점화식사용 프로그램이에서는 다이나믹 프로그래밍인 것같더라고요.
        # n이 1, 2일 때는 점화식 못쓰기에 바로 결과값 반환
        if n == 1:
            return 1
        if n == 2:
            return 2
        # 점화식 처음 세팅
        an_1 = 1
        an_2 = 0
        an = 2
        # 이제 점화식 써가면서 값을 계속 더해주기
        for count in range(n - 2):
            an_1, an_2 = an, an_1
            an = an_1 + an_2
        return an
