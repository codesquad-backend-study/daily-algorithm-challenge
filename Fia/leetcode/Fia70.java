package Fia.leetcode;

import java.util.HashMap;
import java.util.Map;

public class Fia70 { // 70. Climbing Stairs
    public int climbStairs(int n) {
        // n = 1 : 1개
        // n = 2 : 2개
        // n = 3 : 3개 : 1 + 2
        // n = 4 : 5개 : 2 + 3
        // n = 5 : 8개 : 3 + 5
        // n = 6 : 13개 : 5 + 8
        // 자신의 전 그리고 전전을 더한 값이 현재 자신의 경우의 수가 된다는 규칙을 갖는다
        if (n == 0 || n == 1 || n == 2) { // 0, 1, 2인 경우 바로 반환
            return n;
        }

        Map<Integer, Integer> steps = new HashMap<>(); // 1과 2를 미리 넣고 3부터 계산하도록 한다
        steps.put(1, 1);
        steps.put(2, 2);

        for (int i = 3; i <= n; i++) {
            steps.put(i, steps.get(i - 1) + steps.get(i - 2)); // 전과 전전을 더한 값이 현재 자신의 경우의 수
        }

        return steps.get(n);
    }
}
