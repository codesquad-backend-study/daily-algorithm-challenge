import sys

passenger = [0,0,0,0,0]

for i in range(1,5) :
    off, on = map(int,sys.stdin.readline().split())
    passenger[i] = passenger[i-1] - off + on
print(max(passenger))
