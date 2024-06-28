package chap_06;

public class _Quiz_06 {
    public static String getHiddenDate(String data,int index) {
        String re=data.substring(0,index);
        for(int i=0;i<data.length()-index;i++){
            re+="*";
        }
        return re;
    };
    public static void main(String[] args) {
        String name="윤채영";
        String jumin="990409-21000000";
        String tele="010-9913-5931";
        System.out.println(getHiddenDate(name, 1));
        System.out.println(getHiddenDate(jumin, 8));
        System.out.println(getHiddenDate(tele , 9));
    }
}
