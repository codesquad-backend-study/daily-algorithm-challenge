package Fia.baekjoon;

import java.util.*;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class Fia1316 { // 그룹 단어 체커
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int count = scanner.nextInt();
        int answer = 0;

        Pattern pattern = Pattern.compile("(.)\\1+|([a-z])");

        for (int i = 0; i < count; i++) {
            String word = scanner.next();
            Matcher matcher = pattern.matcher(word);

            List<Character> group = new ArrayList<>();
            while (matcher.find()) {
                group.add(matcher.group().charAt(0)); // 정규식을 사용하여 연속되는 문자끼리 자른 후 첫 문자만 List에 넣는다.
            }

            int listSize = group.size(); // List의 크기와
            Set<Character> set = new HashSet<>(group);
            int setSize = set.size(); // 중복을 제거한 Set의 크기를 비교하여

            if (listSize == setSize) { // 같은 경우 그룹 단어로 판단하여 카운트를 증가시킨다.
                answer++;
            }
        }

        System.out.println(answer);
    }
}
