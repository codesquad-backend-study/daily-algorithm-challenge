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
        print(nodeList)
        before = nodeList[:len(nodeList) // 2 ]
        after = nodeList[len(nodeList) // 2:]
        after.reverse()
        for index in range(len(before)):
            if before[index] != after[index]:
                return False
        return True
