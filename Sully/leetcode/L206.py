# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head

        # 파이썬에서 뒤집는 건 그냥 되지만, 자바에서는 이렇게 뒤집었었지!
        # next -> prev -> current
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp

        return prev

        # 재귀 방식 -> 포인터 이용 -> Null일 때 종료
        # if not head:
        #     return None
        #
        # new_head = head
        # if head.next:
        #     new_head = self.reverseList(head.next)
        #     head.next.next = head
        # head.next = None
        #
        # return new_head