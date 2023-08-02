n = int(input())
numbers = list(map(int, input().split()))
numbers.sort()

head = 0
tail = len(numbers) - 1

current = numbers[head] + numbers[tail]
smallest = abs(current)
min_head = head
min_tail = tail

while head < tail:
    if abs(current) < smallest:
        min_head = head
        min_tail = tail
        smallest = abs(current)

    if current > 0:
        tail -= 1
    else:
        head += 1

    current = numbers[head] + numbers[tail]

print(numbers[min_head], numbers[min_tail])
