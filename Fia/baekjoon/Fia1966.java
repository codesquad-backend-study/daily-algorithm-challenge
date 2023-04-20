package Fia.baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.List;
import java.util.stream.Collectors;

public class Fia1966 { // 프린터 큐
    public static void main(String[] args) throws IOException {
        // 각 테스트 케이스는 두 줄
        // 첫 번째 줄에 총 테스트 케이스 수 T
        // 두 번째 줄에 문서의 개수 N / 몇 번째로 인쇄되었는지 궁금한 문서의 현재 Queue 위치 M
        // 세 번째 줄에 N개 문서의 중요도

        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));

        int T = Integer.parseInt(reader.readLine()); // 총 테스트 케이스 수 T

        for (int i = 0; i < T; i++) {
            String[] nm = reader.readLine().split(" ");
            int N = Integer.parseInt(nm[0]); // 문서의 개수 N
            int M = Integer.parseInt(nm[1]); // 몇 번째로 인쇄되었는지 궁금한 문서의 현재 Queue 위치 M
            String[] priority = reader.readLine().split(" ");

            if (N == 1) { // 문서의 개수가 1인 경우 바로 탈출
                System.out.println(N);
                continue;
            }

            List<Integer> list = new ArrayList<>(); // 초기 순서를 저장하는 리스트
            for (int j = 0; j < N; j++) {
                list.add(j);
            }
            LinkedList<Integer> order = new LinkedList<>(list); // 초기 순서
            LinkedList<Integer> queue = Arrays.stream(priority)
                    .map(Integer::parseInt)
                    .collect(Collectors.toCollection(LinkedList::new)); // 우선 순위

            int count = 0; // 몇 번째

            while (!queue.isEmpty()) {
                int first = queue.poll(); // queue 맨 앞 문서의 우선 순위
                int index = order.poll(); // queue 맨 앞 문서의 초기 순서

                boolean highest = true; // 가장 높은 우선 순위인가요?
                for (int k = 0; k < queue.size(); k++) { // 맨 앞의 문서를 빼고 남은 queue 만큼 돌기
                    if (queue.get(k) > first) { // 만약 맨 앞 문서의 우선 순위보다 높은 우선 순위를 갖는 문서가 나오면
                        queue.offer(first); // 맨 앞의 문서를 맨 뒤로
                        order.offer(index);

                        for (int p = 0; p < k; p++) { // 해당 문서 전까지 모두 queue의 맨 뒤로 이동
                            queue.offer(queue.poll());
                            order.offer(order.poll());
                        }

                        highest = false; // 가장 높은 우선 순위가 아니었어요
                        break; // 탈출
                    }
                }

                if (highest == false) { // 다시 돌기
                    continue;
                }

                // 가장 높은 우선 순위의 문서였다면
                count++; // 출력
                if (index == M) { // 초기 순서에서 M번째의 문서인가요?
                    System.out.println(count);
                    break;
                }
            }
        }
    }
}
