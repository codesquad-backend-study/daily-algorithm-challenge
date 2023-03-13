from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:
    current = head
    reverse = None

    while current:
        next = current.next
        current.next = reverse
        reverse = current
        current = next

    return reverse

node5 = ListNode(5)
node4 = ListNode(4, node5)
node3 = ListNode(3, node4)
node2 = ListNode(2, node3)
node1 = ListNode(1, node2)

result = reverseList(node1)

while True:
    if result:
        print(result.val)
        result = result.next
    else:
        break