class Solution {
    boolean solution(String s) {
        int pair = 0;

        for (int i = 0; i < s.length(); i++) {
            if (pair < 0) {
                return false;
            }
            if (s.charAt(i) == '(') {
                pair += 1;
            } else {
                pair -= 1;
            }
        }

        return pair == 0;
    }
}
