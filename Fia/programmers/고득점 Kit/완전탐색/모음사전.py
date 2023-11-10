def solution(word):
    def permutations(array, size):
        results = []

        def generate(temp):
            if len(temp) == size:
                results.append("".join(temp))
                return

            for i in range(len(array)):
                temp.append(array[i])
                generate(temp)
                temp.pop()

        generate([])

        return results

    groups = []

    for i in range(1, 6):
        groups.extend(permutations(['A', 'E', 'I', 'O', 'U'], i))

    groups.sort()

    for i in range(len(groups)):
        if groups[i] == word:
            return i + 1
