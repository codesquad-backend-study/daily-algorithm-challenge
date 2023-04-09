package Fia.baekjoon;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.Scanner;

public class Fia10817 { // 세 수
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        List<Integer> numbers = new ArrayList<>();
        for (int i = 0; i < 3; i++) {
            numbers.add(scanner.nextInt());
        }

        Collections.sort(numbers);
        System.out.println(numbers.get(1));
    }
}
