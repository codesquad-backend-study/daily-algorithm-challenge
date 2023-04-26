room_number = input()
numbers = {}

for number in room_number:
    numbers[number] = numbers.get(number, 0) + 1

numbers['6'] = ((numbers.get('6', 0) + numbers.get('9', 0)) // 2)\
               + ((numbers.get('6', 0) + numbers.get('9', 0)) % 2)
numbers['9'] = 0

print(max(numbers.values()))
