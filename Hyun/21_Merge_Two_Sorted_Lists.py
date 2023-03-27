class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        if list1 is None:
            return list2
        if list2 is None:
            return list1

        node1 = list1
        node2 = list2
        ans = None

        if node1.val <= node2.val:
            ans = node1
            node1 = node1.next
        else:
            ans = node2
            node2 = node2.next

        current = ans

        while True:

            if node1 is None:
                current.next = node2
                break

            if node2 is None:
                current.next = node1
                break

            if node1.val <= node2.val:
                current.next = node1
                node1 = node1.next
            else:
                current.next = node2
                node2 = node2.next

            current = current.next

        return ans
