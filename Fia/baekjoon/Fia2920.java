package Fia.baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Fia2920 { // 음계
    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        String s = reader.readLine();
        String[] split = s.split(" ");

        int[] ints = new int[split.length];
        for (int i = 0; i < split.length; i++) {
            ints[i] = Integer.parseInt(split[i]);
        }

        if (ints[0] == 1) {
            int[] asc = {1, 2, 3, 4, 5, 6, 7, 8};
            if (Arrays.equals(ints, asc)) { // 시간 복잡도 O(n)
                System.out.println("ascending");
                return;
            }
        }

        if (ints[0] == 8) {
            int[] desc = {8, 7, 6, 5, 4, 3, 2, 1};
            if (Arrays.equals(ints, desc)) {
                System.out.println("descending");
                return;
            }
        }

        System.out.println("mixed");
    }
}
