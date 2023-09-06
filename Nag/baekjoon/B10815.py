import sys
nagInput = sys.stdin.readline

nagInput()
sangCrad = list(map(int, nagInput().rstrip().split()))
sang = {i: True for i in sangCrad}
nagInput()
question = list(map(int, nagInput().rstrip().split()))
answer = []
for number in question:
    if number in sang:
        answer.append(str(1))
    else:
        answer.append(str(0))
print(' '.join(answer))
