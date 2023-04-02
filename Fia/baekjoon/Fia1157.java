package Fia.baekjoon;

import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Scanner;
import java.util.stream.Collectors;

public class Fia1157 { // 단어 공부
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String string = scanner.next().toUpperCase();

        if (string.length() == 1) { // 단어의 길이가 1인 경우
            System.out.println(string.toUpperCase());
            return;
        }

        // 1번째 풀이
        Map<Character, Integer> count = new HashMap<>();

        for (int i = 0; i < string.length(); i++) {
            if (count.get(string.charAt(i)) == null) {
                count.put(string.charAt(i), 1);
                continue;
            }

            count.replace(string.charAt(i), count.get(string.charAt(i)) + 1);
        }

        List<Map.Entry<Character, Integer>> entryList = count.entrySet().stream()
                .sorted(Map.Entry.comparingByValue()) // value를 비교하여 정렬
                .collect(Collectors.toList());

        if (entryList.size() == 1) { // 알파벳의 종류가 1개인 경우
            System.out.println(entryList.get(0).getKey());
            return;
        }

        if (entryList.get(entryList.size() - 1).getValue().equals(entryList.get(entryList.size() - 2).getValue())) { // 가장 많이 사용된 알파벳이 여러 개 존재하는 경우
            System.out.println("?");
            return;
        }

        System.out.println(entryList.get(entryList.size() - 1).getKey());

        // 2번째 풀이
        int[] alphabetAscii = new int[26];

        for (int i = 0; i < string.length(); i++) {
            if ('a' <= string.charAt(i) && string.charAt(i) <= 'z') { // 소문자인 경우 소문자 a = 97 즉 a = 0
                alphabetAscii[string.charAt(i) - 'a']++; // 해당 아스키 코드 값의 value++
            } else { // 대문자인 경우
                alphabetAscii[string.charAt(i) - 'A']++; // 대문자 A = 65 즉 A = 0
            }
        }

        int max = -1;
        char alphabet = '?';
        for (int i = 0; i < 26; i++) {
            if (alphabetAscii[i] > max) {
                max = alphabetAscii[i];
                alphabet = (char) (i + 65);
            } else if (alphabetAscii[i] == max) {
                alphabet = '?';
            }
        }

        System.out.println(alphabet);
    }
}
