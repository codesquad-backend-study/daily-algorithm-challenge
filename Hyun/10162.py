given = int(input())

a = given // 300

given %= 300

b = given // 60

given %= 60

c = given // 10

if given % 10 != 0:
    print(-1)
else:
    print(a, b, c)
