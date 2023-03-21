from itertools import combinations

class Solution:
    def climbStairs(self, n: int) -> int:
        # 풀이 1. 시간초과!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        if n == 1:
            return 1
        
        two = n//2
        one = n%2
        way = 0

        while two >= 0:
            total = [2] * (one+two)
            way += len(list(combinations(total,one)))
            two += -1
            one += 2
        return way