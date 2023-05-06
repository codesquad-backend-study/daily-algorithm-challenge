import sys

while True :
    num = sys.stdin.readline()[:-1]
    if num == '0' :
        break
    reverse = num[-1::-1]
    if num == reverse :
        print('yes')
    else :
        print('no')
