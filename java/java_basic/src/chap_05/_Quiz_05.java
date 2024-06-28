package chap_05;

public class _Quiz_05 {
    public static void main(String[] args) {
        int[] shoeSize = new int[10];
        int firstSize=250;
        for (int i=0;i<10;i++) {
            shoeSize[i]=250+(i*5);
        }
        for (int i : shoeSize) {
            System.out.println(i);
        }
    }
}
