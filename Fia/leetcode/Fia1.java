package Fia.leetcode;

import java.util.HashMap;
import java.util.Map;

public class Fia1 {
    // O(log n)의 시간 복잡도를 만족하기 위해서는 Binary Search Tree처럼 경우의 수를 반씩 줄여야 한다.
    // return은 함수 정의의 마지막 문장일 필요는 없다. 반환할 값을 알고 있는 함수의 어느 지점에서라도 이를 반환할 수 있다.
    // 값을 반환하면, 함수의 후속 문장들을 건너뛰면서 함수가 즉시 종료된다.
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> numAndIndex = new HashMap<>();

        for (int i = 0; i < nums.length; i++) {
            if (numAndIndex.containsKey(target - nums[i])) {
                return new int[] {numAndIndex.get(target - nums[i]), i};
            }
            // 만족하는 값이 없을 경우 Map에 저장한다.
            numAndIndex.put(nums[i], i);
        }
        // 컴파일을 위한 return.
        return new int[] {};
    }
}
