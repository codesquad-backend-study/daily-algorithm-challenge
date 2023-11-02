score = {0: "D", 3: "A", 2: "B", 1: "C", 4: "E"}

for _ in range(3):
    yoots = list(map(int, input().split()))
    print(score[sum(yoots)])
