def solution(arr):
    answer = []

    for number in arr:
        if not answer or answer[-1] != number:
            answer.append(number)

    return answer
