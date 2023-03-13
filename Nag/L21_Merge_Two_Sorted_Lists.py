# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        list = []
        
        #노드가 둘다 비어있으면 None 리턴
        if not list1 and not list2:
            return None
        pointer = list1
        
        #리스트에 node 다 넣기
        while pointer:
            list.append(pointer)
            pointer = pointer.next
        pointer = list2
        while pointer:
            list.append(pointer)
            pointer = pointer.next
        #node.val을 기준으로 오름차순 정렬
        list.sort(key = lambda element: element.val)
        #리스트 안의 노드들을 
        for index in range(len(list) - 1):
            list[index].next = list[index + 1]
        return list[0]
