def solution(phone_book):
    def trie_insert(head, string):
        current = head

        for char in string:
            if char not in current[2]:
                current[2][char] = [char, False, {}]

            current = current[2][char]
            if current[1]:
                return True

        current[1] = True
        return False

    phone_book.sort(key=lambda x: len(x))

    head = [-1, False, {}]

    for each in phone_book:
        if trie_insert(head, each):
            return False

    return True
