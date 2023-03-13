package Fia;

import java.util.HashMap;
import java.util.Map;

public class Fia13 {
    public int romanToInt(String s) {
        Map<Character, Integer> values = new HashMap<>(7);
        values.put('I', 1);
        values.put('V', 5);
        values.put('X', 10);
        values.put('L', 50);
        values.put('C', 100);
        values.put('D', 500);
        values.put('M', 1000);

        int answer = 0;
        int count = 0;
        for (int index = 0; index < s.length() - 1; index++) {
            char current = s.charAt(index);
            char next = s.charAt(index + 1);
            if (values.get(current) >= values.get(next)) {
                answer += values.get(current);
            } else if (values.get(current) < values.get(next)) {
                answer += values.get(next) - values.get(current);
                index++;
                count++;
            }
            count++;
        }

        if (count < s.length()) {
            answer += values.get(s.charAt(s.length() - 1));
        }

        return answer;
    }

    public static void main(String[] args) {
        Fia13 fia13 = new Fia13();
        fia13.romanToInt("III");
    }
}
