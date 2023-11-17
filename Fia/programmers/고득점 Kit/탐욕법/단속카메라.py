def solution(routes):
    routes.sort(key=lambda x: min(x))
    limit = max(routes[0])
    count = 1

    for i in range(1, len(routes)):
        if limit < min(routes[i]):
            limit = max(routes[i])
            count += 1
        else:
            limit = min(limit, max(routes[i]))

    return count
