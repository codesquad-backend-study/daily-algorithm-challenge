word_list = []
for _ in range(int(input())):
    word_list.append(input())

word_list = list(set(word_list))
word_list.sort()
word_list.sort(key=len)
print(*word_list, sep="\n")
