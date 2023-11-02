n = int(input())
words = list(set([input() for _ in range(n)]))

words.sort(key=lambda x: (len(x), x))

for word in words:
    print(word)
