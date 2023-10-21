import collections


def solution(priorities, location):
    process_queue = collections.deque([(priority, index) for index, priority in enumerate(priorities)])
    count = 0
    max_priority = max([process[0] for process in process_queue])

    while True:
        process = process_queue.popleft()

        if not process_queue or process[0] >= max_priority:
            count += 1

            if process[1] == location:
                return count

            max_priority = max([process[0] for process in process_queue])
        else:
            process_queue.append(process)
