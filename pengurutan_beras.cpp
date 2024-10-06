#include <bits/stdc++.h>
using namespace std;


int main () {
	int n;
	cin >> n;
	float a[n];
	

	for (int i = 0; i < n;i++) {
		cin >> a[i];
	}
	sort (a, a + n);
	
	if (n % 2 == 0) {
		cout<< fixed<<setprecision(1)<<(a[n /2 - 1] + a[n/2])/2<<endl;
	}
	else {
		cout<<fixed<<setprecision(1)<< a[n/2]<<endl;
	}
	
}
