# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        #두 개의 노드중 하나만 비어도 바로 리턴합니다.(intersection이 있을 수 없습니다)
        if not (headA and headB):
            return None
        AList = []
        BList = []

        #노드를 끝까지 탐색해서 다 리스트에 넣습니다(일부러 순방향으로 넣었습니다)
        pointer = headA
        while pointer:
            AList.append(pointer)
            pointer = pointer.next
        pointer = headB
        while pointer:
            BList.append(pointer)
            pointer = pointer.next

        #맨 끝 노드가 같지 않으면 intersection이 없는 것이기에 바로 리턴 -> 노드는 이제 intersection이 무조건 있습니다
        if AList[-1] != BList[-1]:
            return None

        #기준 설정, 길이가 짧은 노드를 기준으로 합니다(탐색 횟수가 적어집니다)
        standard = []
        if len(AList) < len(BList):
            standard = AList
        else:
            standard = BList
        #맨 뒤부터 탐색하면서(이래서 리스트의 맨끝에 맨 마지막 노드가 있게 설정) intersection을 리턴합니다.
        for index in range(len(standard)):
            if AList[len(AList) - 1 - index] == BList[len(BList) - 1 - index]:
                continue
            return standard[len(standard) - index]
        #반복문을 빠져나왔다는 것은 다 겹친다는 말이므로 첫원소를 리턴해줍니다.
        return standard[0]
