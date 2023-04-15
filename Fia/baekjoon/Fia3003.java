package Fia.baekjoon;

import java.util.Scanner;

public class Fia3003 {
    public static void main(String[] args) { // 1. 킹, 퀸, 룩, 비숍, 나이트, 폰
        Scanner sc = new Scanner(System.in);

        int allHave[] = {1, 1, 2, 2, 2, 8};

        for (int i = 0; i < allHave.length; i++) {
            System.out.print(allHave[i] - sc.nextInt() + " ");
        }

        sc.close();
    }
}
