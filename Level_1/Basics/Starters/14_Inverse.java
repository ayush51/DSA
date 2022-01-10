import java.util.*;

public class Main{

public static void main(String[] args) {
  Scanner scn = new Scanner(System.in);
  int n = scn.nextInt();
  
  int inv = 0; // initializing inverse as 0
  int op = 1; // intialising original position as 1
  
  while(n != 0){
      int od = n%10; //remainder gives the digit at 1st position
      
      int id = op; // original position ---> inverted digit
      int ip = od; // original digit ---> inverted pos
      
      inv = inv + id * (int)Math.pow(10, ip-1); // inverse will be inv + (origonal pos == inv digit) multiplied by 10 to the power (original digit == inverted pos) minus 1
      
      n = n/10;
      op++; 
  }
  
  System.out.println(inv);
 }
}
