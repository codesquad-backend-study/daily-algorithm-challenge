package Fia.leetcode;

public class Fia234 {
    public boolean isPalindrome(ListNode head) {
        StringBuilder builder = new StringBuilder();
        if (head.next == null) { // node가 1개인 경우
            return true;
        }

        while (head != null) {
            builder.append(head.val);
            head = head.next;
        }

        String front = builder.substring(0, builder.length() / 2);
        String back = builder.reverse().substring(0, builder.length() / 2);
        if (front.equals(back)) {
            return true;
        } else {
            return false;
        }
    }
}
