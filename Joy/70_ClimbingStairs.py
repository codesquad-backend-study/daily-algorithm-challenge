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
        # return way
    
        # 풀이 2. 
        if n == 1:
            return 1
        
        step = [0] * (n+1)
        step[1] = 1
        step[2] = 2
        
        for i in range(3, n+1):
            step[i] = step[i-1] + step[i-2]
            
        return step[n]
