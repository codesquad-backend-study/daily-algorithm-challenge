import sys

customInput = sys.stdin.readline

customInput()
rawCard = list(map(int, customInput().rstrip().split()))
card = {}
for number in rawCard:
    if number in card:
        card[number] += 1
    else:
        card[number] = 1
customInput()
question = list(map(int, customInput().rstrip().split()))
answer = []
for number in question:
    if number in card:
        answer.append(card[number])
    else:
        answer.append(0)
print(*answer)
