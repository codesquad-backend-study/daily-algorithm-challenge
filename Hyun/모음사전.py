def solution(word):
    dicts = set()
    alphabets = ['', 'A', 'E', 'I', 'O', 'U']

    def make_words(picks, idx):
        if idx >= 5:
            dicts.add(''.join(picks[:]))
            return

        for ch in alphabets:
            picks.append(ch)
            make_words(picks, idx + 1)
            picks.pop()

    make_words([], 0)
    return sorted(list(dicts)).index(word)
