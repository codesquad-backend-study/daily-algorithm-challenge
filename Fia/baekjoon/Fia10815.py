# 숫자 카드

input()
dictionary = {card: 1 for card in input().split()}

input()
result = [dictionary[card] if dictionary.get(card) else 0 for card in input().split()]

print(*result)
