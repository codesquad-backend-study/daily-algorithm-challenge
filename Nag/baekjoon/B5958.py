cnt = int(input())
inputList = [input() for i in range(cnt)]
split = [list(filter(None, str.split('X'))) for str in inputList]

for splitList in split:
    score = 0
    for str in splitList:
        num = len(str)
        score += num * (num + 1) // 2
    print(score)
