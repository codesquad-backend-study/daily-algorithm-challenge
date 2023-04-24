package Fia.baekjoon;

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Fia2747 { // 피보나치 수
    public static void main(String[] args) {
        List<Integer> numbers = new ArrayList<>();
        numbers.add(0);
        numbers.add(1);

        Scanner scanner = new Scanner(System.in);
        int N = scanner.nextInt();
        for (int i = 2; i <= N; i++) {
            numbers.add(numbers.get(i - 2) + numbers.get(i - 1));
        }
        System.out.println(numbers.get(numbers.size() - 1));
    }
}
