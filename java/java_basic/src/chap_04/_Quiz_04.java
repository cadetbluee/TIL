package chap_04;

public class _Quiz_04 {
    public static void main(String[] args) {
        int fee=4000;
        int time=5;
        String car="sma";
        int totalFee=0;
        while (totalFee<30000){
            totalFee+=fee;
            time--;
            if (time==0){
                break;
            }
            if (totalFee>30000){
                totalFee=30000;
            }
        }
        if(car=="small" || car=="disabled"){
            System.out.println(totalFee/2+"원");
        }else{
            System.out.println(totalFee +"원");
        }
    }
}
