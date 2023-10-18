import collections


def solution(priorities, location):
    counter = collections.Counter(priorities)

    queue = collections.deque()
    for idx, priority in enumerate(priorities):
        queue.append((idx, priority))

    count = 0
    max_val = 9
    while queue:
        while max_val not in counter:
            max_val -= 1

        pop = queue.popleft()

        if pop[1] == max_val:
            count += 1
            counter[max_val] -= 1
            if counter[max_val] == 0:
                del counter[max_val]

            if pop[0] == location:
                return count
        else:
            queue.append(pop)
