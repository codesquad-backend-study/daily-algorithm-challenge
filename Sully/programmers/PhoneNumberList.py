from typing import List


# 접두어가 "존재하면" False 리턴
def solution(phone_book: List[str]) -> bool:
    phone_map = {}
    for phone in phone_book:
        phone_map[phone] = 1

    for phone in phone_book:
        tmp = ''
        for p in phone:
            tmp += p
            if tmp in phone_map and tmp != phone:
                return False

    return True


print(solution(["119", "97674223", "1195524421"]))
print(solution(["123", "456", "789"]))
print(solution(["12", "123", "1235", "567", "88"]))
