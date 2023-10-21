import java.util.*;

public class Solution {
    public List<Integer> solution(int []arr) {
        List<Integer> answer = new ArrayList<>();

        for (int number : arr) {
            if (answer.isEmpty() || answer.get(answer.size() - 1) != number) {
                answer.add(number);
            }
        }

        return answer;
    }
}
