# 수 찾기
import collections

int(input())

dictionary = collections.defaultdict(bool)

for number in input().split():
    dictionary[number] = True

int(input())

for X in input().split():
    print(int(dictionary[X]))
