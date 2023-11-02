word = input()
dic = {chr(key): 0 for key in range(ord('a'), ord('z') + 1)}
for char in word:
    dic[char] += 1
for key in dic:
    dic[key] = str(dic[key])
print(' '.join(dic.values()))
