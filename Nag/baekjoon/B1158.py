n, k = map(int, input().split())
numbers = [i + 1 for i in range(n)]
answer = []
start = k - 1
while numbers:
    copy = numbers[:]
    for index in range(start, len(numbers), k):
        answer.append(numbers[index])
        copy.remove(numbers[index])
        start = index + k
    start -= len(numbers)
    numbers = copy
print('<' + ', '.join(map(str, answer)) + '>')
