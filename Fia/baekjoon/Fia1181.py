def sorting_words():
    count = int(input())
    words = []

    for _ in range(count):
        words.append(input())

    words = list(set(words))

    print(*sorted(words, key=lambda word: (len(word), word)), sep="\n")


sorting_words()
