package Fia.baekjoon;

import java.util.Scanner;

public class Fia8958 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int count = scanner.nextInt();

        for (int i = 0; i < count; i++) {
            String result = scanner.next();
            result = result.replaceAll("X+", "X");
            String[] split = result.split("X");
            int point = 0;
            for (String s : split) {
                for (int j = 1; j <= s.length(); j++) {
                    point += j;
                }
            }
            System.out.println(point);
        }
    }
}
