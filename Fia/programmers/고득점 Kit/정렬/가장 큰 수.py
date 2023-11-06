def solution(numbers):
    str_numbers = ''.join(sorted([str(number) for number in numbers], reverse=True, key=lambda x: x * 3))

    if str_numbers.startswith('0'):
        str_numbers = str(int(str_numbers))

    return str_numbers
