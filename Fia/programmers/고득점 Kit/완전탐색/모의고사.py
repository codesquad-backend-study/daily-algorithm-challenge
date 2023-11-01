def solution(answers):
    supozas = {0: [1, 2, 3, 4, 5],
               1: [2, 1, 2, 3, 2, 4, 2, 5],
               2: [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]}

    correct_count = [0, 0, 0]

    def mark(supoza, number, answer):
        if supozas[supoza][number % len(supozas[supoza])] == answer:
            correct_count[supoza] += 1

    for number, answer in enumerate(answers):
        mark(0, number, answer)
        mark(1, number, answer)
        mark(2, number, answer)

    answer = []
    max_correct = max(correct_count)

    for index, count in enumerate(correct_count):
        if max_correct == count:
            answer.append(index + 1)

    return sorted(answer)
