from collections import deque

N, K = map(int, input().split())
q = deque(range(1, N + 1))
yose = []

# N명이 원을 이루면서 앉아 있음
# 순서대로 K번째 사람을 제거 -> 이 제거되는 순서를 계속 저장

# while len(yose) != N:
#     if seq >= len(a):
#         seq -= len(a)
#
#     seq += 2
#     yose.append(a[seq])
#     del a[seq]

# 리스트랑 deque 이용해서 계속 해보다가 시간만 날리는 거 같아서 deque 하나만
while q:
    for _ in range(K - 1):
        # 왼쪽에 있는 걸 빼고 맨뒤에 계속 추가해줘
        q.append(q.popleft())

    # 그 뺀 것을 순열에 순서대로 추가
    yose.append(q.popleft())

print('<', end='')
print(', '.join(map(str, yose)), end='')
print('>')
