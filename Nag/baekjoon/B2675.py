cnt = int(input())
inputList = [list(input().split()) for i in range(cnt)]
for element in inputList:
    iteration, str = int(element[0]), element[1]
    output = ''
    for c in str:
        output = output + c * iteration
    print(output)
