def pick(idx, sour, bitter):
    if idx >= len(ingredients):
        if bitter != 0:
            diff.append(abs(sour - bitter))
        return

    pick(idx + 1, sour, bitter)
    pick(idx + 1, sour * ingredients[idx][0], bitter + ingredients[idx][1])


n = int(input())
diff = []
ingredients = [list(map(int, input().split())) for _ in range(n)]

pick(0, 1, 0)
print(min(diff))


# 그냥 재귀로 풀래 ㅋㅋ
