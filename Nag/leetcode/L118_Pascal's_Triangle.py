class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        # 콤비네이션 함수 구현(nCr)
        def combination(n: int, r: int) -> int:
            nCopy= n
            rCopy= r
            module = 1
            denominator = 1
            
            #n과 r이 같거나 r이 0이면 1반환
            if n == r:
                return 1
            if r == 0:
                return 1
            #r의 두배값이 n보다 크면 더 빠른 연산을 위해 r값을 바꿔서 재귀로 호출
            if r * 2 > n:
                return combination(n, n - r)
            
            #실제 연산부분
            for count in range(r):
                module *= nCopy
                denominator *= rCopy
                nCopy -= 1
                rCopy -= 1
            return module // denominator
        
        answer = []
        
        #2중 반복문으로 2중리스트 생성후 반환
        for count in range(numRows):
            row = []
            for index in range(count + 1):
                element = combination(count, index)
                row.append(element)
            answer.append(row)
        return answer
