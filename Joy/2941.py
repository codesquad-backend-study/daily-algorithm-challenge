import sys

word = sys.stdin.readline()[:-1]

croatia = ['dz=', 'c=', "c-", "d-", "lj", "nj", "s=", "z="]
for c in croatia :
    word = word.replace(c,'*')

print(len(word))