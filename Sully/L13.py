class Solution:
    # 로마자 예외: 4, 9, 40, 90, 400, 900
    # ex) IX: 1 + 8 = 9 -> X가 원래 10인데 -2단계가 된 값인 8로 처리가 됨
    # 위와 같은 규칙 이용
    def romanToInt(self, s: str) -> int:
        sum_value = 0
        before_symbol = ''

        for i in range(len(s)):
            current_symbol = s[i]
            # 위에 써놓은 예외 처리 (-2단계)
            if before_symbol == 'I' and current_symbol == 'V':
                sum_value += 3
            elif before_symbol == 'I' and current_symbol == 'X':
                sum_value += 8
            elif before_symbol == 'X' and current_symbol == 'L':
                sum_value += 30
            elif before_symbol == 'X' and current_symbol == 'C':
                sum_value += 80
            elif before_symbol == 'C' and current_symbol == 'D':
                sum_value += 300
            elif before_symbol == 'C' and current_symbol == 'M':
                sum_value += 800
            # 현재 로마 문자 다 더해주기
            elif current_symbol == 'I':
                sum_value += 1
            elif current_symbol == 'V':
                sum_value += 5
            elif current_symbol == 'X':
                sum_value += 10
            elif current_symbol == 'L':
                sum_value += 50
            elif current_symbol == 'C':
                sum_value += 100
            elif current_symbol == 'D':
                sum_value += 500
            elif current_symbol == 'M':
                sum_value += 1000
            # 현재 문자가 이전 문자가 되고, 다음 반복 때 현재 문자가 갱신됨
            before_symbol = current_symbol

        return sum_value

# dict() 이용
# class Solution:
#     def romanToInt(self, s: str) -> int:
#         translations = {
#             "I": 1,
#             "V": 5,
#             "X": 10,
#             "L": 50,
#             "C": 100,
#             "D": 500,
#             "M": 1000
#         }
#
#         s = s.replace("IV", "IIII").replace("IX", "VIIII")
#         s = s.replace("XL", "XXXX").replace("XC", "LXXXX")
#         s = s.replace("CD", "CCCC").replace("CM", "DCCCC")
#
#         number = 0
#         for char in s:
#             number += translations[char]
#         return number
