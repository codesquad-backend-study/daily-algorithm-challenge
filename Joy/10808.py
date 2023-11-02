import sys

alpha = { chr(i):0 for i in range(97,123)}

word = sys.stdin.readline()[:-1]

# for s in word :
#     alpha[s] += 1

for s in alpha : # 단어를 기준으로 for문 돌릴때랑 시간 똑같음
    alpha[s] = word.count(s)

for s in alpha :
    print(alpha[s], end=" ")