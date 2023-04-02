input = input()
dic = {}
for char in input:
    if char not in dic:
        dic[char] = input.index(char)
for cnt in range(26):
    if chr(ord("a") + cnt) not in dic:
        dic[chr(ord("a") + cnt)] = -1
dic = dict(sorted(dic.items()))
for key in dic:
    print(dic[key], end=' ')
