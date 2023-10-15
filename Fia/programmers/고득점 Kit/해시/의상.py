def solution(clothes):
    closet = {}

    for cloth in clothes:
        name, type = cloth

        if type not in closet.keys():
            closet[type] = 0

        closet[type] += 1

    if len(closet.keys()) == 1:
        return len(clothes)

    result = 1
    for value in closet.values():
        result *= value + 1

    return result - 1
