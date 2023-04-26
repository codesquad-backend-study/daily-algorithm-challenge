import sys
import math

room = sys.stdin.readline()[:-1]

num = [0 for i in range(10)]

for s in room :
    num[int(s)] += 1

six = num[6]
nine = num[9]
tmp = math.ceil((six+nine)/2)

num[6] = 0
num[9] = 0

ans = max(num)
ans = max(ans, tmp)
print(ans)