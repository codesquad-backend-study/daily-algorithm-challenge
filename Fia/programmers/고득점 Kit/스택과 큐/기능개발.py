def solution(progresses, speeds):
    def calculate_days_to_work(index):
        days = (100 - progresses[index]) // speeds[index]

        if (100 - progresses[index]) % speeds[index] > 0:
            days += 1

        return days

    answer = []

    days_to_release = calculate_days_to_work(0)
    release = 1

    for i in range(1, len(progresses)):
        days_to_work = calculate_days_to_work(i)

        if days_to_release >= days_to_work:
            release += 1
        else:
            answer.append(release)
            days_to_release = days_to_work
            release = 1

    answer.append(release)

    return answer
