import java.util.*;
  
  public class Main{
  
  public static void main(String[] args) {
    Scanner scn = new Scanner(System.in);
    int n = scn.nextInt();
    
    int nod = 0;
    int temp = n;
    while (temp!= 0){
        temp = temp/10;
        nod++; // nod means number of digits
    }
    int div = (int)Math.pow(10, nod - 1); // div is 10 to the power of ( nod -1)
    while (div!=0){ 
        int q = n / div; // here q is the quotient that gives first digit to be printed
        System.out.println(q);
        n = n%div; // n becomes remainder of n/div
        div = div/10; // div reduces to div/10
        
    }
    
   }
  }
