# 예제만 통과 ,,
# N = int(input())
# words = list(input() for _ in range(N))
# dict_words = {chr(i): 0 for i in range(ord('a'), ord('z') + 1)}
# # dict_copied = dict_words
# group_count = 0
# last_alp = ''
# isGroup = True
# tmp_count = 0
#
# for i in range(N):
#     isGroup = True
#     tmp_count = 0
#     dict_words = {key: 0 for key in dict_words}
#     # dict_words = dict_copied
#     last_alp = ''
#
#     for current_alp in words[i]:
#         # 딕셔너리의 value 값이 0보다 크거나, 마지막 알파벳이 현재의 알파벳과 다르다면 그룹 단어가 아니라는 의미
#         if dict_words[current_alp] > 0 and last_alp != current_alp and last_alp != '':
#             print(i, '번째', current_alp, dict_words[current_alp], 'last_alp:', last_alp, 'current_alp:',
#                   current_alp)
#             isGroup = False
#             break
#
#         tmp_count += 1
#         dict_words[current_alp] = tmp_count
#         last_alp = current_alp
#
#     if isGroup is True:
#         group_count += 1
#
# print(group_count)

# 그냥 평소에 하던 대로 index로 풀자 도저히 안 풀림
# 그룹 단어가 아닐 경우 빼는 방식으로 접근

N = int(input())
group_count = N
words = list(input() for _ in range(N))

for i in range(N):
    for j in range(0, len(words[i]) - 1):
        # 현재랑 바로 그 후가 다를 때
        if words[i][j] != words[i][j + 1]:
            # 현재의 바로 전까지의 단어에 미래의 단어가 있을 경우
            if words[i][j + 1] in words[i][:j]:
                # 있으면 그룹 단어가 아니므로 빼주자
                group_count -= 1
                break

print(group_count)

