import sys

# sys.stdin.readline(): BufferedReader와 동일
# 근데 이렇게 선언해주면 안 됨.. []가 붙어서 출력되게 됨
# 이것 땜에 1시간 가까이 날렸는데 June의 도움으로 해결
# array = [list(map(int, sys.stdin.readline().split())) for _ in range(9)]

array = []

for _ in range(9):
    array.append(int(sys.stdin.readline()))

# 출력
print(max(array))
print(array.index(max(array)) + 1)
