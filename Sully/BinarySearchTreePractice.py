# 이진 탐색 트리 구현 연습 (파이썬)
# https://geonlee.tistory.com/72

class Node(object):
    # 생성자 정의
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinarySearchTree(object):
    # 생성자 정의
    def __init__(self):
        self.root = None

    # 삽입 -> 트리에 새 원소를 추가할 수 있도록 해줌 (재귀 이용)
    # 새로 추가할 원소의 값을 현재 노드의 값과 비교하여, 왼쪽과 오른쪽 중 알맞은 위치로 노드를 옮겨 가며 삽입 위치 확인
    def _insert_value(self, node, data):
        if node is None:
            node = Node(data)
        else:
            if data <= node.data:
                node.left = self._insert_value(node.left, data)
            else:
                node.right = self._insert_value(node.right, data)
        return node

    def insert(self, data):
        self.root = self._insert_value(self.root, data)
        return self.root is not None

    # 탐색 -> 원하는 값을 존재 유무를 확인
    # 재귀의 값의 대소 관계 비교를 통해 구현
    def _find_value(self, root, key):
        if root is None or root.data == key:
            return root is not None
        elif key < root.data:
            return self._find_value(root.left, key)
        else:
            return self._find_value(root.right, key)

    def find(self, key):
        return self._find_value(self.root, key)

    # 삭제 -> 삭제할 Node의 자식이 없으면 문제가 없지만, 자식이 하나인 경우엔 자식 노드를 삭제한 노드 위치로 가져옴
    # 노드의 자식이 두 개일 때 ->
    # 왼쪽 서브 트리와 오른쪽 서브 트리를 각각 A, B라고 했을 때,
    # B에서 가장 왼쪽 아래에 위치한 자손을 가져옴
    # 이 원소는 A의 모든 원소들보다는 크면서, B의 나머지 원소보다 작기 때문에 해당 노드를 가져오는 것
    def _delete_value(self, node, key):
        if node is None:
            return node, False

        deleted = False
        if key == node.data:
            deleted = True
            if node.left and node.right:
                parent, child = node, node.right
                while child.left is not None:
                    parent, child = child, child.left
                child.left = node.left
                if parent != node:
                    parent.left = child.right
                    child.right = node.right
                node = child
            elif node.left or node.right:
                node = node.left or node.right
            else:
                node = Node
        elif key < node.data:
            node.left, deleted = self._delete_value(node.left, key)
        else:
            node.right, deleted = self._delete_value(node.right, key)
        return node, deleted

    def delete(self, key):
        self.root, deleted = self._delete_value(self.root, key)
        return deleted


# 예제로 확인
array = [40, 4, 34, 45, 14, 55, 48, 13, 15, 49, 47]

bst = BinarySearchTree()
for x in array:
    bst.insert(x)

# 탐색
print(bst.find(15))
print(bst.find(17))

# 삭제
print(bst.delete(55))
print(bst.delete(14))
print(bst.delete(11))
