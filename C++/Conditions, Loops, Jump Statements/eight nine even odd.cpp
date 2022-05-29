#include <bits/stdc++.h>
using namespace std;

int main() {
  string one[] = { "", "one ", "two ", "three ", "four ", 
                 "five ", "six ", "seven ", "eight ", 
                 "nine "
               }; 

int t;
while (t--){

int a; 
cin >> a;
int b;
cin >> b;
	for (int n = a; n<=b; ++n){
		if (n<=9 && n >=1){
			cout << one[n]<< endl;
		}
		else if ( n > 9 && n %2 == 0){
			cout << "even" << endl;
		}
		else if ( n > 9 ){
			cout << "odd"<< endl;
		}
	}
    return 0;
}
}








