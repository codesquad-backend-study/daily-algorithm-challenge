package Fia.baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Fia1152 {
    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));

        String s = reader.readLine();
        s = s.replaceAll("\\s+", " "); // 공백이 2개 연속인 경우 1개로 수정
        s = s.strip(); // 앞 뒤 공백 제거
        String[] strings = s.split(" ");

        if (strings.length == 1 && strings[0] == "") { // 공백만 있는 경우
            System.out.println(0);
            return;
        }

        System.out.println(strings.length);
    }
}
