N = int(input())
data = input()
K = 0
pow = N - 1
for i in range(N):
    if data[i] == '1':
        K += 2 ** pow
    pow -= 1

count = 0
while K != 0:
    K = K - (K & (~K + 1))
    count += 1
print(count)

------------------------------------
# 마지막 1인 비트를 비틀어서 제끼기 때문에
# 1의 개수를 세면 된다.
N = int(input())
K = input()
print(K.count('1'))
