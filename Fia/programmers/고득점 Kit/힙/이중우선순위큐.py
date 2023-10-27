import heapq


def solution(operations):
    min_heap = []
    max_heap = []

    for operation in operations:
        command, number = operation.split()

        if command == "I":
            heapq.heappush(min_heap, int(number))
            heapq.heappush(max_heap, -int(number))
        elif command == "D" and min_heap:
            if number == "1":
                max_number = heapq.heappop(max_heap)
                min_heap.remove(-max_number)
                heapq.heapify(max_heap)
            else:
                min_number = heapq.heappop(min_heap)
                max_heap.remove(-min_number)
                heapq.heapify(min_heap)

    return [-heapq.heappop(max_heap), heapq.heappop(min_heap)] if max_heap else [0, 0]
