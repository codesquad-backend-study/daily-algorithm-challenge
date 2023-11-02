alphabet = [0] * 26
word = input()
for ch in word:
    alphabet[ord(ch) - ord("a")] += 1
print(*alphabet)