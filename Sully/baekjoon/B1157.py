# 계속 바꿔서 10번 이상 제출했는데 타임초과
# string 쓴 게 잘못이었다
# 딕셔너리{현재 문자열: 카운트}로 가자 그냥
'''
import sys

S = sys.stdin.readline().upper()
count_max = 0
answer = ''

for s in S:
    tmp_count = S.count(s)

    # 이미 같으면 여러 개 존재한다는 의미
    # 하지만 문자열이 같을 수 있으니 그걸 체크해야 함
    if count_max == tmp_count and answer != s:
        answer = '?'
        break

    if count_max < tmp_count:
        count_max = tmp_count

        # 현재 문자열 저장
        answer = s


print(answer)
'''

#################################

# 와 또 실패 스프링 해야 되는데
'''
import sys

S = sys.stdin.readline().upper()
count_max = 0
dict_count = {}
final = ''

for s in S:
    S_count = S.count(s)
    # 만약에 없으면 계속 넣어주면 되고
    if s not in dict_count:
        dict_count[s] = S_count

    # 이제부터 카운트 비교해주면 되지
    if S_count > count_max:
        count_max = S_count
        # max값을 딕셔너리에 계속 갱신
        dict_count[s] = count_max
        final = s

# dict_count에 똑같은 value가 존재한다면 final 변수에 '?'를 저장
# 딕셔너리 value -> list 변환
# count_max에 저장되어 있는 값들이 몇개가 있는지 세고, 2 이상이면 '?' 저장
if list(dict_count.values()).count(count_max) > 1:
    final = '?'

print(final)
'''

################################

import sys

S = sys.stdin.readline().upper()

# 딕셔너리 초기화
# {}으로 두지 말고 key는 A부터 Z까지로, value는 0으로 둬야지 더 편함
dict_count = {chr(i): 0 for i in range(ord('A'), ord('Z') + 1)}

# 각 요소별로 count 저장해두기
for s in S:
    dict_count[s] += 1

# 그걸 가지고 value의 최댓값 찾기
count_max = max(dict_count.values())

# 그 최댓값을 가진 문자 찾기
# dict_count에 똑같은 value가 존재한다면 final 변수에 '?'를 저장
# 딕셔너리 value -> list 변환
# count_max에 저장되어 있는 값들이 몇개가 있는지 세고, 1이 아니면 '?' 저장
final = ''
if list(dict_count.values()).count(count_max) == 1:
    final = max(dict_count, key=dict_count.get)
else:
    final = '?'

print(final)
