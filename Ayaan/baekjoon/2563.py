# 겹치는 부분 넓이 구해서 빼줄려다가 실패
# 겹치는 부분이 2중 3중이면 안됨...
# N = int(input())
# area = N * 100
# paper = []
# for _ in range(N):
#     paper.append(list(map(int, input().split())))

# for i in range(0, N-1):
#     std = paper[i]
#     for j in range(i+1, N):
#         target = paper[j]
#         # 겹치는 부분이 있는지 체크
#         if std[0] + 10 <= target[0] or std[0] >= target[0] + 10:
#             continue
#         if std[1] + 10 <= target[1] or std[1] >= target[1] + 10:
#             continue
        
#         # 겹치는 부분 넓이를 구해서 빼줌
#         width = 0
#         height = 0
#         if std[0] < target[0]:
#             width = std[0] + 10 - target[0]
#         else:
#             width = target[0] + 10 - std[0]
#         if std[1] < target[1]:
#             height = std[1] + 10 - target[1]
#         else:
#             height = target[1] + 10 - std[1]
        
#         area -= width * height
# print(area)


# 100X100 이차원 배열을 만들어서 푼다.
# 0으로 초기화
area = [[0 for _ in range(100)] for _ in range(100)]
for _ in range(int(input())):
    x, y = map(int, input().split())
    # 사각형 만큼 1로 넣어줌
    for i in range(x, x+10):
        for j in range(y, y+10):
            area[i][j] = 1

result = 0
for i in range(100):
    result += sum(area[i])

print(result)