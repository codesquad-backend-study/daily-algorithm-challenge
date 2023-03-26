package Fia.leetcode;

import java.util.HashMap;
import java.util.Map;

public class Fia136 {
    public int singleNumber(int[] nums) {
        Map<Integer, Integer> duplicatedChecker = new HashMap<>();

        for (int num : nums) {
            if (duplicatedChecker.containsKey(num)) {
                duplicatedChecker.remove(num);
            } else {
                duplicatedChecker.put(num, 1);
            }
        }

        Object[] object = duplicatedChecker.keySet().toArray();

        return (int) object[0];
    }
}
