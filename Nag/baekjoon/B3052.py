remain = set()
for _ in range(10):
    number = int(input())
    remain.add(number % 42)
print(len(remain))
