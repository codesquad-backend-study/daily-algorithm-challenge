import sys

# 풀이 1. 580ms
word = sys.stdin.readline()

lst = [ s.upper() for s in word[:-1]]

max_chr = '?'
max_cnt = 0

for chr in set(lst) :
    tmp = lst.count(chr)
    if tmp > max_cnt :
        max_chr = chr
        max_cnt = tmp
    elif tmp == max_cnt :
        max_chr = '?'

print(max_chr)

# 풀이 2. 시간초과
word = sys.stdin.readline().upper()

result = ''
max = 0

for s in word:
    n = word.count(s)
    if n > max:
        max = n
        result = s
    elif n == max:
        result = '?'
        
print(result)

# 풀이 3. 68ms A-Z까지 전부 검사하는데 제일 빠르다. 왜??????????
word = sys.stdin.readline().upper()

result = ''
max = 0

for i in range(65,91):
    n = word.count(chr(i))
    if n > max:
        max = n
        result = chr(i)
    elif n == max:
        result = '?'
        
print(result)