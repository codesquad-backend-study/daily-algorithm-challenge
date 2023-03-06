class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: ListNode) -> [ListNode]:
        before = None
        current = head
        # None.next 실행시 에러발생! 주의하기
        while current:
            after = current.next
            current.next = before
            before = current
            current = after
        # 바뀐 head 반환
        return before