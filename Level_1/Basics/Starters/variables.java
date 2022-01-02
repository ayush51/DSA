import java.util.*;

public class Main{
    
    public static void main(String[] args){
        int x  = 15;
        int y = 10;
        int sum = x+y;
        
        System.out.println("sum is " + sum);
        
        int v1 = x/y;
        int v2 = y/x;
        int v3 = x % y ;
        
        System.out.println(v1 + "," + v2 + "," + v3);
        
        /// exp
        int exp = x * y / (x + y) ;
        System.out.println(exp);
    }
}
