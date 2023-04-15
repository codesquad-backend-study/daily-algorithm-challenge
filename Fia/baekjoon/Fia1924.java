package Fia.baekjoon;

import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

public class Fia1924 { // 2007년
    public static void main(String[] args) {
        // 일 % 7 = 0 : MON
        Map<Integer, String> week = Map.of(1, "MON",
                2, "TUE",
                3, "WED",
                4, "THU",
                5, "FRI",
                6, "SAT",
                0, "SUN");

        Map<Integer, Integer> month = new HashMap<>(); // 누적 날짜 수
        month.put(1, 0);
        month.put(2, month.get(1) + 31);
        month.put(3, month.get(2) + 28);
        month.put(4, month.get(3) + 31);
        month.put(5, month.get(4) + 30);
        month.put(6, month.get(5) + 31);
        month.put(7, month.get(6) + 30);
        month.put(8, month.get(7) + 31);
        month.put(9, month.get(8) + 31);
        month.put(10, month.get(9) + 30);
        month.put(11, month.get(10) + 31);
        month.put(12, month.get(11) + 30);

        Scanner scanner = new Scanner(System.in);
        int M = scanner.nextInt();
        int D = scanner.nextInt();

        System.out.println(week.get((month.get(M) + D) % 7));
    }
}
