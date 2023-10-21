import java.util.*;

class Solution {
    public List<Integer> solution(int[] progresses, int[] speeds) {
        List<Integer> answer = new ArrayList<>();

        int release = 1;
        int daysToRelease = (100 - progresses[0]) / speeds[0];
        if ((100 - progresses[0]) % speeds[0] > 0) {
            daysToRelease++;
        }

        for (int i = 1; i < progresses.length; i++) {
            int daysToWork = (100 - progresses[i]) / speeds[i];
            if ((100 - progresses[i]) % speeds[i] > 0) {
                daysToWork++;
            }

            if (daysToRelease >= daysToWork) {
                release++;
            } else {
                answer.add(release);
                daysToRelease = daysToWork;
                release = 1;
            }
        }

        answer.add(release);

        return answer;
    }
}
