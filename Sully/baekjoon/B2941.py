word = input()

# 크로아티아 알파벳은 중복되지 않으니까 집합으로 저장하자

# alphabets = {'c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z='}

# cnt = 0
# tmp = ''
# for w in word:
#     tmp += w
#     # 이거 O(1)임
#     if tmp in alphabets:
#         cnt += 1
#         tmp = w
#     elif tmp not in alphabets:
#         if len(tmp) == 2:
#             tmp = w
#         elif len(tmp) == 2 and tmp == 'dz':
#             continue
#         # dz를 보고 dz=가 아닐까? 하며 돌려보내줬는데(continue) 결국 dz=가 아닌 경우
#         elif len(tmp) == 3:
#             tmp = w

# 문제를 잘못 이해하고 있었음
# 그냥 일반 알파벳과 크로아티아 알파벳을 분리해서 생각하면 간단하게 풀리는 문제였음

# set 자료형으로 처리하면 틀린 로직임 (딕셔너리로 되는 이유는 순서 존재 딕셔너리기 때문)
# O(1)을 만들기 위해 value가 0인 딕셔너리로 처리하자 :)
# alphabets = {'c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z='}
alphabets = {'c=': 0, 'c-': 0, 'dz=': 0, 'd-': 0, 'lj': 0, 'nj': 0, 's=': 0, 'z=': 0}

for alp in alphabets:
    word = word.replace(alp, '@')

print(len(word))
