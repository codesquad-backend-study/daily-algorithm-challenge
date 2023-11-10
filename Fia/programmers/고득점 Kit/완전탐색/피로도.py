def solution(k, dungeons):

    def calculate(energy, group):
        count = 0

        for dungeon in group:
            if energy >= dungeon[0]:
                count += 1
                energy -= dungeon[1]

        return count

    def permutations(array, size):
        answer = [0]
        used = [False] * len(array)

        def generate(temp):
            if len(temp) == size:
                answer[0] = max(answer[0], (calculate(k, temp)))
                return

            for i in range(len(array)):
                if not used[i]:
                    temp.append(array[i])
                    used[i] = True
                    generate(temp)
                    used[i] = False
                    temp.pop()

        generate([])

        return answer[0]

    return permutations(dungeons, len(dungeons))

print(solution(80, [[80, 20], [50, 40], [30, 10]]))

# 순열이 만들어지는 과정 ex. [[80, 20], [50, 40], [30, 10]]

# [[80, 20]]
# [[80, 20], [50, 40]]
# [[80, 20], [50, 40], [30, 10]]
# [[80, 20], [50, 40]]
# [[80, 20]]
# [[80, 20], [30, 10]]
# [[80, 20], [30, 10], [50, 40]]
# [[80, 20], [30, 10]]
# [[80, 20]]
# []
# [[50, 40]]
# [[50, 40], [80, 20]]
# [[50, 40], [80, 20], [30, 10]]
# [[50, 40], [80, 20]]
# [[50, 40]]
# [[50, 40], [30, 10]]
# [[50, 40], [30, 10], [80, 20]]
# [[50, 40], [30, 10]]
# [[50, 40]]
# []
# [[30, 10]]
# [[30, 10], [80, 20]]
# [[30, 10], [80, 20], [50, 40]]
# [[30, 10], [80, 20]]
# [[30, 10]]
# [[30, 10], [50, 40]]
# [[30, 10], [50, 40], [80, 20]]
# [[30, 10], [50, 40]]
# [[30, 10]]
# []
