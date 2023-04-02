package Fia.baekjoon;

import java.util.Scanner;

public class Fia2562 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int maxNumber = 0;
        int index = 0;

        for (int i = 1; i <= 9; i++) {
            int number = scanner.nextInt();
            if (number > maxNumber) {
                maxNumber = number;
                index = i;
            }
        }

        System.out.println(maxNumber);
        System.out.println(index);
    }
}
