package Fia.baekjoon;

import java.util.Scanner;

public class Fia2675 { // 문자열 반복
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int count = scanner.nextInt();

        StringBuilder builder = new StringBuilder();

        for (int i = 0; i < count; i++) {
            int repeat = scanner.nextInt();
            String string = scanner.next();
            for (int j = 0; j < string.length(); j++) {
                String s = String.valueOf(string.charAt(j)).repeat(repeat);
                builder.append(s);
            }
            System.out.println(builder);
            builder.setLength(0);
        }
    }
}
