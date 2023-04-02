package Fia.baekjoon;

public class Fia4673 { // self number
    public static void main(String[] args) {
        int range = 10000;
        boolean[] check = new boolean[range + 1];

        for (int i = 1; i < range; i++) {
            int numberD = findD(i);
            if (numberD <= range) { // D number가 범위 안의 숫자인 경우 true로 변경한다.
                check[numberD] = true;
            }
        }

        StringBuilder builder = new StringBuilder();

        for (int i = 1; i < range; i++) {
            if (!check[i]) {
                builder.append(i).append(System.lineSeparator());
            }
        }

        System.out.println(builder);
    }

    private static int findD(int number) {
        int numberD = number;

        while (number > 0) {
            numberD += number % 10; // 숫자를 하나씩 더하여 D number를 구한다.
            number /= 10; // 더한 숫자 제거
        }

        return numberD;
    }
}
