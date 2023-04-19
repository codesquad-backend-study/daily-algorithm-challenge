package Fia.baekjoon;

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Fia7568 { // 덩치
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int N = scanner.nextInt();

        List<List<Integer>> dung = new ArrayList<>(); // 일단 리스트에 담기
        for (int i = 0; i < N; i++) {
            int height = scanner.nextInt();
            int weight = scanner.nextInt();

            List<Integer> temp = new ArrayList<>();
            temp.add(height);
            temp.add(weight);
            dung.add(temp);
        }

        StringBuilder builder = new StringBuilder();
        for (int i = 0; i < N; i++) {
            int upCount = 1; // 나의 덩치 순위
            for (int j = 0; j < N; j++) {
                if (i == j) { // 나의 정보면 패스
                    continue;
                }
                boolean weight = dung.get(i).get(1) < (dung.get(j).get(1)); // 나보다 몸무게가 많이 나가는가
                boolean height = dung.get(i).get(0) < (dung.get(j).get(0)); // 나보다 키가 큰가
                if (weight && height) { // 두 가지 조건을 만족하는 경우
                    upCount++; // 나의 덩치 순위는 뒤로
                }
            }
            builder.append(upCount).append(" ");
        }
        System.out.println(builder);
    }
}
