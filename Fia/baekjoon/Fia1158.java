package Fia.baekjoon;

import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class Fia1158 { // 요세푸스 문제
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int N = scanner.nextInt();
        int K = scanner.nextInt();

        Queue<Integer> queue = new LinkedList(); // 일단 큐에 모든 사람 넣기
        for (int i = 1; i <= N; i++) {
            queue.offer(i);
        }

        StringBuilder builder = new StringBuilder("<");
        while (queue.size() != 0) {
            for (int i = 1; i < K; i++) {
                queue.offer(queue.poll()); // K번째 전까지 빙글빙글
            }
            if (queue.size() == 1) {
                builder.append(queue.poll()).append(">"); // 마지막 K번째 사람 제거
                break;
            }
            builder.append(queue.poll()).append(", "); // K번째 사람 제거
        }
        System.out.println(builder);
    }
}
