package Fia.baekjoon;

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Fia2775 {
    public static void main(String[] args) { // 부녀회장이 될테야
        // N층 : 1호 2호 3호 ...
        // 0층 : 1   2   3   4   5
        // 1층 : 1   3   6   10  15
        // 2층 : 1   4   10  20  35
        // 3층 : 1   5   15  35  70
        // 4층 : 1   6   21  56  126

        Scanner scanner = new Scanner(System.in);
        int T = scanner.nextInt(); // 테스트 케이스 수

        List<Integer> floors = new ArrayList<>(); // 층
        List<Integer> rooms = new ArrayList<>(); // 호
        int maxFloor = 0; // 가장 높은 층
        int maxRoom = 0; // 가장 큰 호
        for (int i = 0; i < T; i++) { // 정보를 미리 입력 받는다.
            int f = scanner.nextInt(); // 층
            if (f > maxFloor) {
                maxFloor = f;
            }
            int r = scanner.nextInt(); // 호
            if (r > maxRoom) {
                maxRoom = r;
            }
            floors.add(f); // 층
            rooms.add(r); // 호
        }

        List<List<Integer>> apt = new ArrayList<>(); // 한 번만 계산하기 위해
        List<Integer> zeroLine = new ArrayList<>(); // 0층 미리 입력
        for (int i = 1; i <= maxRoom; i++) {
            zeroLine.add(i);
        }
        apt.add(zeroLine);

        for (int i = 0; i < maxFloor; i++) {
            List<Integer> l = new ArrayList<>(); // 현재 층
            List<Integer> under = apt.get(i); // 아래 층
            l.add(1); // 1호는 항상 1명
            for (int j = 1; j < maxRoom; j++) {
                l.add(l.get(j - 1) + under.get(j)); // 자신의 왼쪽 호과 자신의 아래 층을 더한 값
            }
            apt.add(l); // 아파트에 층 추가
        }

        for (int i = 0; i < floors.size(); i++) { // 가져와서 출력
            System.out.println(apt.get(floors.get(i)).get(rooms.get(i) - 1));
        }
    }
}
