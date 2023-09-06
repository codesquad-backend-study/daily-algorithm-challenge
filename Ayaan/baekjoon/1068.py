N = int(input())
parent_list = list(map(int, input().split()))
delete = int(input())

tree = [[] for _ in range(N)]
for i in range(N):
    # -1인 경우 루트 노드이고 삭제될 노드인 delete는 연결 x
    if parent_list[i] != -1 and i != delete:
            tree[parent_list[i]].append(i)

def delete_dfs(x):
    # delete 자식 노드 모두 삭제
    for i in range(len(tree[x])):
        node = tree[x].pop()
        delete_dfs(node)
    # 삭제된 노드 False 처리
    tree[x].append(False)

delete_dfs(delete)

leaf_cnt = 0
for i in range(N):
    if not tree[i]:
        leaf_cnt += 1
print(leaf_cnt)
