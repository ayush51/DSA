import java.util.*;

public class Main{
    
public static void main(String[] args) {
 
Scanner scn = new Scanner(System.in);
int t = scn.nextInt();

for(int i = 0; i<t ; i++){
    int n = scn.nextInt();

int count = 0;
    for(int div = 1; div<=n; div++){
        if (n % div == 0){
            count++;
        }
        }
        
        if ( count == 2){
            System.out.println("prime")   ; 
            }
            else {
                System.out.println("not prime");
            }
            
        }
        
    }

}

// Complexity of above is t*n = 10^4*10^9 = 10^13 --- hence time limit exceeded

import java.util.*;

public class Main{
    
public static void main(String[] args) {
 
Scanner scn = new Scanner(System.in);
int t = scn.nextInt();

for(int i = 0; i<t ; i++){
    int n = scn.nextInt();

int count = 0;
    for(int div = 2; div * div <=n; div++){
        if (n % div == 0){
            count++;
        }
        }
        
        if ( count == 0 && n != 1){
            System.out.println("prime")   ; 
            }
            else {
                System.out.println("not prime");
            }
            
        }
        
    }

}



/// complexity 10^4 * root(10^9) = 10^9 



 
