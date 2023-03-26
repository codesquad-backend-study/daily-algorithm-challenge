package Fia.leetcode;

public class Fia21 {
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        if (list1 == null && list2 == null) {
            return null;
        }
        if (list1 == null) {
            return list2;
        }
        if (list2 == null) {
            return list1;
        }

        ListNode head;
        if (list1.val <= list2.val) {
            head = list1;
            merge(head, list1.next, list2);
        } else {
            head = list2;
            merge(head, list1, list2.next);
        }
        return head;
    }

    public ListNode merge(ListNode previous, ListNode list1, ListNode list2) {
        if (list1 == null && list2 == null) {
            previous.next = null;
            return null;
        }
        if (list1 == null) {
            previous.next = list2;
            return null;
        }
        if (list2 == null) {
            previous.next = list1;
            return null;
        }
        if (list1.val <= list2.val) {
            previous.next = list1;
            return merge(list1, list1.next, list2);
        } else {
            previous.next = list2;
            return merge(list2, list1, list2.next);
        }
    }
}
