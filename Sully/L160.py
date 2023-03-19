# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    # 2개의 링크드리스트 교차하는 부분 찾기
    # 만약, 교차하는 부분 없으면 0 리턴
    def getIntersectionNode(self, headA, headB):
        # 교차되는 부분 없으므로 0 리턴
        if headA is None or headB is None:
            return None

        # 현재 A, B가 계속 바뀔 것이므로 변수 지정
        currentA = headA
        currentB = headB

        # 현재의 A와 B가 다를 때 계속 반복문 돌아주기
        while currentA != currentB:
            # 현재 A가 있으면 다음으로 가고
            if currentA:
                currentA = currentA.next
            # A가 없으면 B로 감
            else:
                currentA = headB

            # B도 위와 똑같이 진행
            if currentB:
                currentB = currentB.next
            else:
                currentB = headA

        # 결론은 A와 B가 같은 지점에서 만날 때 반복문이 빠져나오도록 했다.
        # 직접 예제를 가지고 노드의 하나씩 이동시켜보면 이해할 수 있다.
        # "else"에서의 로직이 핵심 로직 -> A나 B가 null이 되면 그 상대 node로 이동한다는 뜻
        # 위와 같은 방식으로 결국 맞물리는 지점이 생기게 됨
        return currentA
