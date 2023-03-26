package Fia.leetcode;

public class Fia206 {
    public ListNode reverseList(ListNode head) {
        if (head == null) {
            return null;
        }

        ListNode previous = null; // 맨 마지막 null부터 시작하여 next를 바꾸는 방법 // 시간 복잡도 : O(n)
        ListNode current = head;

        while (current != null) {
            ListNode next = current.next;
            current.next = previous;
            previous = current;
            current = next;
        }

        return previous;
    }
}

class ListNode {
    int val;
    ListNode next;

    ListNode() {
    }

    ListNode(int val) {
        this.val = val;
    }

    ListNode(int val, ListNode next) {
        this.val = val;
        this.next = next;
    }
}
