package Fia.baekjoon;

import java.util.Scanner;

public class Fia25304 { // 영수증
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        final int TOTAL = scanner.nextInt();
        final int N = scanner.nextInt();

        int sum = 0;
        for (int i = 0; i < N; i++) {
            int price = scanner.nextInt(); // 가격
            int count = scanner.nextInt(); // 구매 수량
            sum += price * count; // 계속 더하기
        }

        if (TOTAL == sum) {
            System.out.println("Yes");
            return;
        }
        System.out.println("No");
    }
}
