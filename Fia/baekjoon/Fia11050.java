package Fia.baekjoon;

import java.util.Scanner;

public class Fia11050 { // 이항 계수 = nCk = n개 중 k개를 뽑는 조합의 수
    // dp	k=0	k=1	k=2 ...
    // n=0	 1	 0	 0
    // n=1	 1	 1	 0
    // n=2	 1	 2	 1
    // n=3	 1	 3	 3
    // n=4	 1	 4	 6
    // ...
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int N = scanner.nextInt();
        int K = scanner.nextInt();

        int[][] dp = new int[N + 1][K + 1];

        for (int i = 0; i <= N; i++) {
            dp[i][0] = 1;
        }

        for (int i = 1; i <= N; i++) {
            for (int j = 1; j <= K; j++) {
                dp[i][j] = dp[i - 1][j] + dp[i - 1][j - 1];
            }
        }

        System.out.println(dp[N][K]);
    }
}
