# {몸무게, 키} 딕셔너리 만들기
N = int(input())
weight_height = []
for _ in range(N):
    tmp_list = list(map(int, input().split()))
    weight_height.append((tmp_list[0], tmp_list[1]))

# 메인
# answer = []
# tmp_answer = 1
# for k in range(len(weight_height) - 1):
#     # weight = weight_height[k][0]
#     # height = weight_height[k][1]
#
#     if weight_height[k][0] < weight_height[k][1] and weight_height[k + 1][0] < weight_height[k + 1][1]:
#         tmp_answer += 1
#
#     answer.append(tmp_answer)
#
# print(' '.join(map(str, answer)))

answer = []
# 아 한번에 처리하면 안 되고 2번 돌아줘야 되는구나
for cur in range(len(weight_height)):
    tmp_answer = 1
    for nxt in range(len(weight_height)):
        if weight_height[cur][0] < weight_height[nxt][0] and weight_height[cur][1] < weight_height[nxt][1]:
            tmp_answer += 1

    answer.append(tmp_answer)

print(' '.join(map(str, answer)))
