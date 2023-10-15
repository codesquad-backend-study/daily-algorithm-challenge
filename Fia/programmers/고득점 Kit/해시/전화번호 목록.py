def solution(phone_book):
    trie = {}

    for phone_number in phone_book:
        current = trie

        for number in phone_number:
            numbers = current.keys()

            if number not in numbers:
                current[number] = {}

            if current[number] and "Y" in current[number].keys():
                return False

            current = current[number]

        numbers = current.keys()

        if len(numbers) > 1:
            return False

        if numbers and "Y" not in numbers:
            return False

        current["Y"] = True

    return True
