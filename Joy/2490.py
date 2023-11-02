import sys

count_1 = {0:'D', 1:'C', 2:'B', 3:'A', 4:'E'}

for  i in range(3) :
    yut = sys.stdin.readline()
    tmp = yut.count('1')
    print(count_1[tmp])

