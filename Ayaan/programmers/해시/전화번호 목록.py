def solution(phone_book):
    phone_book.sort()

    dict = {}
    length = len(phone_book[0])
    dict[phone_book[0]] = 1
    for i in range(1, len(phone_book)):
        phone = phone_book[i]
        if dict.get(phone[:length]):
            return False
        dict[phone] = 1
        length = len(phone)
    return True


print(solution(["119", "97674223", "1195524421"]))
