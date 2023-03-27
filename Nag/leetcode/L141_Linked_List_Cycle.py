# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        dic = {}
        pointer = head

        # 어제 투썸에서 딕셔너리로 저장하는 것을 활용해서 딕셔너리로 만듬
        while pointer is not None:
            if pointer in dic:
                return True
            dic[pointer] = True
            pointer = pointer.next
        return False
