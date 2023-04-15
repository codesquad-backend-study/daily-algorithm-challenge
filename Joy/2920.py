import sys

scale = sys.stdin.readline()[:-1]

result = 'mixed'

if scale == "1 2 3 4 5 6 7 8" :
    result = 'ascending'
elif scale == "8 7 6 5 4 3 2 1" :
    result = 'descending'

print(result)