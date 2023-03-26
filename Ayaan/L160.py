# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# 이중 반복문으로 모두 탐색
# 시간초과
# def getIntersectionNode(headA: ListNode, headB: ListNode) -> Optional[ListNode]:    
#     while headA:
#         target = headB
#         while target:
#             if headA == target:
#                 return headA
#             target = target.next
#         headA = headA.next
#     return None

def getIntersectionNode(headA, headB):    
    # 둘 다 리스트로 만든다.
    listA = []
    while headA:
        listA.append(headA)
        headA = headA.next
    listB = []
    while headB:
        listB.append(headB)
        headB = headB.next
    
    result = None
    # 뒤에서부터 확인해서 값이 같은 교집합 부분은 result에 담는다.
    # 값이 달라지면 그 값의 next가 답이 된다.
    while listA and listB:
        if listA[-1] == listB[-1]:
            result = listA[-1]
        else:
            return listA[-1].next
        listA.pop(-1)
        listB.pop(-1)
    return result

node1 = ListNode(5)
node2 = ListNode(4)
node2.next = node1
node3 = ListNode(8)
node3.next = node2
node4 = ListNode(1)
node4.next = node3
node5 = ListNode(1)
node5.next = node3
node6 = ListNode(4)
node6.next = node4
node7 = ListNode(6)
node7.next = node5
node8 = ListNode(5)
node8.next = node7

result = getIntersectionNode(node6, node8)
print(result)