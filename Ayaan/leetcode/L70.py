# dynamic programming을 사용한다?
# result는 이전값 더하기 이전값의 이전값이 된다?
def climbStairs(self, n: int) -> int:
    dp1 = 1
    dp2 = 2

    if n <= 2:
        return n

    result = 0
    for i in range(3, n+1):
        result = dp1 + dp2
        dp1 = dp2
        dp2 = result
    return result

def climbStairs2(n):
    prev_prev = 1
    prev = 1
    cur = 1
    
    for i in range(1, n):
        # 현재 개수는 이전값 + 이전값의 이전값
        cur = prev + prev_prev
        # 이전값의 이전값은 이전값으로 변경
        prev_prev = prev
        # 이전값은 이전값 + 이전값의 이전값으로 변경
        prev = cur
    
    return cur

# 규칙을 찾는 것이 중요한 것 같다.
# 이런 문제는 많이 풀어보면서 규칙 찾는법을 배워야겠따.