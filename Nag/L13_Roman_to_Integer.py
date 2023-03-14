class Solution:
    def romanToInt(self, s: str) -> int:
        num = []
        answer = 0
        #String 을 int list로 변환
        for c in s:
            if c == 'I':
                num.append(1)
            if c == 'V':
                num.append(5)
            if c == 'X':
                num.append(10)
            if c == 'L':
                num.append(50)
            if c == 'C':
                num.append(100)
            if c == 'D':
                num.append(500)
            if c == 'M':
                num.append(1000)
        #탐색하면서 숫자로 변환
        #로마숫자 문자열이 검증되어 있어서 앞의 숫자가 뒤의 숫자보다 작으면 뺴도 됩니다.
        for index in range(len(num)):
            if index == len(num) - 1:
                answer += num[index]
                continue
            if num[index] < num[index + 1]:
                answer -= num[index]
            else:
                answer += num[index]
        return answer
