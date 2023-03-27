# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:

        # 풀이 1. 테스트케이스 통과, 시간초과
        if not headA or not headB:
            return None
        
        curA, curB = headA, headB
        listA = []

        while curA != None : 
            listA.append(curA)
            curA = curA.next

        while curB != None :
            if curB in listA :
                return curB
            curB = curB.next       
        return None
    
        # 풀이 2. 통과
        if not headA or not headB:
            return None
    
        curA = headA
        curB = headB
    
        while curA != curB:
            curA = curA.next if curA else headB
            curB = curB.next if curB else headA
        
        return curA