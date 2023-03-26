class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        nodes = {}

        if head is None or head.next is None:
            return False

        while head is not None:
            if head in nodes:
                return True
            nodes[head] = 1
            head = head.next

        return False
    