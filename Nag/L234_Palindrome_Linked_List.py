# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        nodeList = []
        pointer = head

        while pointer is not None:
            nodeList.append(pointer.val)
            pointer = pointer.next
        #리스트 슬라이싱, 노드가 홀수개 있으면 가장 중앙에 있는 값은 신경 안써도 됩니다(어차피 비교 안해도 되니까)
        before = nodeList[:len(nodeList) // 2 ]
        after = nodeList[len(nodeList) // 2:]
        after.reverse()
        for index in range(len(before)):
            if before[index] != after[index]:
                return False
        return True
