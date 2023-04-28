answer = []
for _ in range(3):
    status = list(map(int, input().split()))
    dic = {0: "D", 1: "C", 2: "B", 3: "A", 4: "E"}
    answer.append(dic[sum(status)])
for s in answer:
    print(s)
