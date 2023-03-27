class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head

        tail = head
        nodes = []

        while tail.next is not None:
            nodes.append(tail)
            tail = tail.next

        current_node = tail
        while nodes:
            node = nodes.pop()
            current_node.next = node
            current_node = node

        head.next = None

        return tail