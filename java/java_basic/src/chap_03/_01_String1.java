package chap_03;

public class _01_String1 {
    public static void main(String[] args) {
        String s="chaeyoung Yoon";
        System.out.println(s.toLowerCase());
        System.out.println(s.toUpperCase());
        System.out.println(s.contains("chae"));
        System.out.println(s.contains("yegong"));
        System.out.println(s.indexOf("ch")); //처음위치아니면 -1
        System.out.println(s.lastIndexOf("o")); //마지막위치
        System.out.println(s.startsWith("ch"));
        System.out.println(s.endsWith("."));
        System.out.println(s.substring(2));
    }
}
