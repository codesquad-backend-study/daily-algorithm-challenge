correct = [1, 1, 2, 2, 2, 8]

given = list(map(int, input().split()))

for i in range(len(given)):
    print(correct[i] - given[i], end=" ")
