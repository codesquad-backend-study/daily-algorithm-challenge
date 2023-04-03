package Fia.baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Fia5622 { // 다이얼
    public static void main(String[] args) throws IOException {
        // 다이얼 동작 방식 이해가 안돼서 엄마한테 여쭤봄 ㅋㅋ
        // 전화를 걸기 위해서 필요한 '최소' 시간을 구하는 프로그램 : 왜 굳이 '최소'라고 명시한 걸까요? 필요한 시간은 하나로 정해져 있는게 아닌가? 할머니가 다이얼을 천~천~히 돌릴 수 있어서 그런가...

        // 문자를 아스키 넘버로 확인하여 해당 숫자 범위 내에 있는지 확인하는 방식
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        int time = 0;

        String alphabets = reader.readLine();
        for (int i = 0; i < alphabets.length(); i++) {
            char c = alphabets.charAt(i);
            if ('W' <= c) {
                time += 10;
            } else if ('T' <= c) {
                time += 9;
            } else if ('P' <= c) {
                time += 8;
            } else if ('M' <= c) {
                time += 7;
            } else if ('J' <= c) {
                time += 6;
            } else if ('G' <= c) {
                time += 5;
            } else if ('D' <= c) {
                time += 4;
            } else if ('A' <= c) {
                time += 3;
            }
        }
        System.out.println(time);
    }
}
