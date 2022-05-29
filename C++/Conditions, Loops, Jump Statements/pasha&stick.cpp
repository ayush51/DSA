#include<bits/stdc++.h>
using namespace std;

int main (){

int n;
cin >> n;
 
 if (n%2 != 0){
 	cout << 0;
 }
 else {
 	int count = 0;
 	for (int a =1; a<=n/4 ; ++a){
     int x = 0;
     int x = n/2 - a;
     if (x==a){
	break;
}
     count ++;
 	}
 	cout << count ;

 }
}

#include<bits/stdc++.h>
using namespace std;

int main (){

int n;
cin >> n;
 
 if (n%2){cout << 0;}
 n/=2;
 if(n%2) {cout<<n/2;}
 else {cout<<n/2 -1;}
 return 0;
}



