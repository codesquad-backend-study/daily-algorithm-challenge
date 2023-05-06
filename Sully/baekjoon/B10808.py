S = input()

# if문 a부터 z까지 하면 풀리긴 하지만 아스키코드 써보자

# key: alp, value: 0
alp = {}
for c in range(ord('a'), ord('z') + 1):
    alp[chr(c)] = 0

for s in S:
    alp[s] += 1

for value in alp.values():
    print(value, end=' ')
