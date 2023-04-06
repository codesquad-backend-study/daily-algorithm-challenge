package Fia.baekjoon;

import java.util.Scanner;

public class Fia1193 { // 분수 찾기
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int x = scanner.nextInt();
        int numerator = 1; // 분자
        int denominator = 1; // 분모

        int count = 1; // 계산 수
        int max = 2; // 최대 숫자
        while (count < x) { // x번 계산 했다면 while 탈출
            numerator = 1; // 분자에 1을 넣고
            denominator = max; // 분모에 최대 숫자를 넣는다
            count++; // 계산 +1회 처리한다
            if (count == x) { // x번 계산 했다면 while 탈출
                break;
            }
            for (int i = max - 1; i > 0; i--) {
                numerator++; // 분자는 +1 반복
                denominator--; // 분모는 -1 반복
                count++; // 계산 +1회 처리한다
                if (count == x) { // x번 계산 했다면 for 탈출
                    break;
                }
            }
            max++; // 최대 숫자 값 증가
        }

        if ((denominator + numerator) % 2 == 0) { // 두 수의 합이 짝수인 경우
            System.out.println(denominator + "/" + numerator); // 분자와 분모의 위치를 바꿔서 출력한다
            return;
        }

        // 두 수의 합이 홀수인 경우
        System.out.println(numerator + "/" + denominator);
    }
}
