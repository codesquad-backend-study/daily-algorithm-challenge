import sys

word = sys.stdin.readline()

for i in range(97,123) :
    char = chr(i)
    times = word.find(char)
    print(times, end=" ")
