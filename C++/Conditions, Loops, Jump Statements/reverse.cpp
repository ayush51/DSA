	#include <bits/stdc++.h>
	using namespace std;

	int main() {
	int t;
	cin >> t;
	while (t--){
		int n,r;
		cin >> n;
		while (n >0){
			r = n%10;
			cout << r;
			n=n/10;
		}
		cout << endl;
	}

	}








