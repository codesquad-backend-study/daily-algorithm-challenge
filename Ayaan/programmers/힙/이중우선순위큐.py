import heapq


def solution(operations):
    q = []
    for operation in operations:
        operation = operation.split()
        if operation[0] == 'I':
            heapq.heappush(q, int(operation[1]))
        else:
            if q:
                if operation[1] == '1':
                    q.remove(max(q))
                else:
                    heapq.heappop(q)

    if q:
        return [max(q), q[0]]
    else:
        return [0, 0]


solution(["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"])
