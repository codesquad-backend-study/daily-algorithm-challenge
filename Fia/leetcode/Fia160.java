package Fia.leetcode;

public class Fia160 {
    // 풀이 실패

    // 중간 교차 지점부터 같은 형태를 갖는다.
    // 즉 교차 노드 이전에 존재할 수 있는 길이의 차이만 채워주면 값을 비교하기 쉽다.
    // 연결 리스트 A의 길이가 10이고 연결 리스트 B의 길이가 5일 때
    // A + B 즉 15로 총 길이를 맞추면 follow up의 O(n + m)의 연산 횟수를 만족할 수 있다.
    public ListNode getIntersectionNode(ListNode headA, ListNode headB) {
        if (headA == null || headB == null) {
            return null;
        }

        ListNode pointerA = headA;
        ListNode pointerB = headB;
        while (pointerA != pointerB) { // 둘 다 null로 끝나면 교차 노드가 없음을 의미한다.
            pointerA = pointerA != null ? pointerA.next : headB;
            pointerB = pointerB != null ? pointerB.next : headA;
        }
        return pointerA;
    }
}
