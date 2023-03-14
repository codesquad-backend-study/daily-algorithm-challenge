class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        numbers = []
        result = 0
        for ro in s:
            numbers.append(roman[ro])

        for i in range(len(numbers)-1):
            result = result+numbers[i] if numbers[i] >= numbers[i+1] else result-numbers[i]
        result += numbers[-1]
        return result