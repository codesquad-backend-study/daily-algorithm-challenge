class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        a = []

        while head is not None:
            a.append(head.val)
            head = head.next

        if len(a) == 1:
            return True

        if len(a)%2 == 1:
            return a[:len(a)//2 + 1] == a[len(a)//2:][::-1]

        return a[:len(a)//2] == a[len(a)//2:][::-1]

