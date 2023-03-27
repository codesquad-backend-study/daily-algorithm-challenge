package Fia.baekjoon;

import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

public class Fia10809 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String word = scanner.next();

        Map<Character, Integer> dictionary = new HashMap<>();
        for (int i = 0; i < word.length(); i++) {
            if (!dictionary.containsKey(word.charAt(i)))
            dictionary.put(word.charAt(i), i);
        }

        StringBuilder builder = new StringBuilder();

        for (int i = 'a'; i <= 'z'; i++) {
            if (dictionary.get((char) i) == null) {
                builder.append("-1 ");
                continue;
            }
            builder.append(dictionary.get((char) i)).append(" ");
        }

        System.out.println(builder.toString().stripTrailing());
    }
}
