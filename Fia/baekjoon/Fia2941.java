package Fia.baekjoon;

import java.util.Scanner;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class Fia2941 { // 크로아티아 알파벳
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String word = scanner.next();

        Pattern pattern = Pattern.compile("(c=)|(c-)|(dz=)|(d-)|(lj)|(nj)|(s=)|(z=)|([a-z])");
        Matcher matcher = pattern.matcher(word);

        int count = 0;
        while (matcher.find()) { // 문자열의 앞에서부터 일치하는 것을 하나씩 find 한다. 다음 find는 추출한 문자열 다음부터 시작한다.
            count++; // 정규식과 일치하는 문자열을 find하면 count를 증가한다.
        }

        System.out.println(count);
    }
}
