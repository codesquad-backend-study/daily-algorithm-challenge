dic = {}
str = input().upper()
for c in str:
    if c in dic:
        dic[c] += 1
    else:
        dic[c] = 1
sortedList = sorted(dic.items(), key=lambda x: x[1])
if len(sortedList) > 1 and sortedList[-1][1] == sortedList[-2][1]:
    print("?")
else:
    print(sortedList[-1][0])
