package chap_01;

public class _07_TypeCasting {
    public static void main(String[] args) {
        int score=93;
        // score=score+98.3;
        System.out.println(score);
        System.out.println((float)score);
        System.out.println((double)score);
        float score_f=93.3F;
        double score_d=98.8;
        score_d=(double)93+98.8;
        String i=String.valueOf(93);
        System.out.println(i);
        int i1=Integer.parseInt("93");
    }
}