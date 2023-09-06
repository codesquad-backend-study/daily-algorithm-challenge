import sys

# 이것도 너무 많이 해주면 메모리 초과 발생
sys.setrecursionlimit(10 ** 4)


# 왼 -> 왼 -> 왼 -> 쭉 가다가 더 자식 노드가 없을 때 오른쪽 방문
def dfs(left, right):

    if left > right:
        return

    div = right + 1
    root = array[left]

    for cur in range(left + 1, right + 1):
        if root < array[cur]:
            div = cur
            break

    dfs(left + 1, div - 1)
    dfs(div, right)

    answer.append(root)


array = []
while True:
    try:
        array.append(int(sys.stdin.readline().rstrip()))
    except:
        break

answer = []
dfs(0, len(array) - 1)
print(*answer)