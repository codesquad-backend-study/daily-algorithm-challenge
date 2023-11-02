# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pointer = head
        list = []
        
        if not pointer:
            return None
        while pointer.next:
            list.append(pointer)
            pointer = pointer.next
        answer = pointer
        list = list[::-1]
    
        while list:
            list[0].next = None
            pointer.next = list[0]
            pointer = pointer.next
            del list[0]
        return answer
