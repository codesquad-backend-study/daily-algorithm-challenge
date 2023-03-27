import sys

numbers =[]
for i in range(9):
    numbers.extend(list(map(int,sys.stdin.readline().split()))) 

maxNum = max(numbers)
idx = numbers.index(maxNum)

print(maxNum)
print(idx+1)

