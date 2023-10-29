import heapq


def solution(operations):
    max_heap = []
    min_heap = []

    counter = 0

    for op in operations:
        ins, number = op.split()
        number = int(number)

        if ins == 'I':
            counter += 1
            heapq.heappush(max_heap, (-number))
            heapq.heappush(min_heap, number)
        elif ins == 'D' and counter > 0:
            if number == 1:
                heapq.heappop(max_heap)
            else:
                heapq.heappop(min_heap)
            counter -= 1

            if counter == 0:
                max_heap = []
                min_heap = []

    if not counter:
        return [0, 0]

    return [-max_heap[0], min_heap[0]]
