package Fia.baekjoon;

import java.util.Scanner;

public class Fia10250 {
    public static void main(String[] args) { // ACM 호텔
        Scanner scanner = new Scanner(System.in);
        int test = scanner.nextInt();

        for (int i = 0; i < test; i++) {
            int h = scanner.nextInt();
            int w = scanner.nextInt();
            int n = scanner.nextInt();

            if (n % h == 0) { // 최대 높이인 경우
                System.out.println(h * 100 + n / h);
                continue;
            }

            int floor = (n % h) * 100; // 앞의 두 자리
            int room = (n / h) + 1; // 뒤의 두 자리

            System.out.println(floor + room);
        }
    }
}
