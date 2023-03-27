package Fia.leetcode;

import java.util.HashMap;

public class Fia141 {
    public boolean hasCycle(ListNode head) {
        HashMap<ListNode, Integer> nodes = new HashMap<>();
        if (head == null) {
            return false;
        }
        ListNode currentNode = head;
        int index = 0;
        while (true) {
            nodes.put(currentNode, index);
            if (nodes.get(currentNode.next) != null) {
                return true;
            }
            if (currentNode.next != null) {
                currentNode = currentNode.next;
            }
            if (currentNode.next == null) {
                return false;
            }
        }
    }
}
