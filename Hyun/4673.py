check = [True] * 10001

for i in range(1, 10001):
    check[i + sum(map(int, list(str(i)))) if i + sum(map(int, list(str(i)))) < 10001 else 0] = False

for idx in range(10001):
    if check[idx]:
        print(idx)




