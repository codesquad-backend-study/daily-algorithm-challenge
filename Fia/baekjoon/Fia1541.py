# 잃어버린 괄호
# 시간 제한 2초
# 0-9와 +와 - 사용, 처음과 마지막은 문자, 연속해서 2개 이상의 연산자 존재 X, 5자리 이상의 숫자 X, 0이 수의 시작 O
# 식의 길이 <= 50
import re

expression = input()
token = re.findall('[0-9]+|[+-]', expression)  # 토큰화

if '-' not in token:  # - 연산이 없는 경우 총합을 바로 반환
    print(sum(int(number) for number in token if number.isdigit()))
    exit()

number = []
index = 0
while index < len(token):
    t = token[index]
    if t.isdigit():
        number.append(int(t))
        index += 1
    else:
        index += 1
        if t == '+':  # + 연산이 나온 경우 + 연산의 이전 값과 이후 값을 더하여 number에 추가
            number.append(number.pop() + int(token[index]))
            index += 1  # 이후 값을 사용했으므로 한번 건너뛰기

result = number[0]
for n in number[1:]:  # - 연산만 남았으므로 계산 후 반환
    result -= n

print(result)
