public class hello {
public static void main(String thefm[]) 
{
    int count=0,len;
    int num[]={12,16,25,1,4528};
    String ch[];
    for(int i=0;i<5;i++){
        ch[i]= Integer.toString(num[i]);
    }
    for(int i=0;i<5;i++){
        len = ch[i].length();
        while(len[i]%2==0){
            count=count+1;
        }
    }
    System.out.println("count of numbers which contains the even number of digits :"+count);
    
}    
}
