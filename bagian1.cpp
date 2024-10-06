#include <bits/stdc++.h>
using namespace std;

int a,b,hasil,x;

int f (int hasil) {
	
	while (hasil%10==0) {
	   hasil/=10;
	}
	 return hasil%=10;
}

int main () {
	cin>>a>>b;
	int hasil=1;
	for (int i=a;i<=b;i++ ) {
		hasil*=i;
	}
	
	cout<<f(hasil)<<endl;
}
