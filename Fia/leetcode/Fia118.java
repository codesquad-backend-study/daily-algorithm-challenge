package Fia.leetcode;

import java.util.ArrayList;
import java.util.List;

public class Fia118 {
    public List<List<Integer>> generate(int numRows) {
        List<List<Integer>> answer = new ArrayList<>(); // 맨 위를 넣고 시작
        List<Integer> top = new ArrayList<>();
        top.add(1);
        answer.add(top);

        for (int i = 1; i < numRows; i++) {
            List<Integer> row = new ArrayList<>();
            for (int j = 0; j <= i; j++) {
                if (j == 0) { // 왼쪽 끝
                    row.add(1);
                }
                if (j == i) { // 오른쪽 끝
                    row.add(1);
                }
                if (j > 0 && j < i) { // 가운데
                    row.add(answer.get(i - 1).get(j - 1) + answer.get(i - 1).get(j));
                }
            }
            answer.add(row);
        }
        return answer;
    }
}
