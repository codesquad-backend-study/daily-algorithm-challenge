class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:

        a_dict = {}

        while headA is not None:
            a_dict[headA] = 1
            headA = headA.next

        while headB is not None:
            if headB in a_dict:
                return headB

            headB = headB.next

        return None
