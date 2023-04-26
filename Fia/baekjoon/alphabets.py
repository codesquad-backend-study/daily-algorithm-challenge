word = input()
dictionary = {}

for char in word:
    dictionary[char] = dictionary.get(char, 0) + 1

for alphabet in range(ord('a'), ord('z') + 1):
    print(dictionary.get(chr(alphabet), 0), end=" ")
