package Fia.baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;

public class Fia10773 {
    public static void main(String[] args) throws IOException {
        // 제로
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        int K = Integer.parseInt(reader.readLine());
        int sum = 0; // 결과 총합

        Stack<Integer> numbers = new Stack<>();
        for (int i = 0; i < K; i++) {
            int number = Integer.parseInt(reader.readLine());
            if (number == 0) {
                sum -= numbers.pop(); // 가장 최근의 수를 stack에서 제거하면서 sum에서 빼기
                continue;
            }
            numbers.add(number);
            sum += number;
        }
        System.out.println(sum);
    }
}
