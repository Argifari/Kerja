#include <bits/stdc++.h>
#define II long long
using namespace std;

II c, t,nilai;

int main () {
	
	cin>>c;
	
	for (int i=1;i<=c;i++) {
		cin>>t;
		nilai=((t+1)*t)/2;
		cout<<"Case #"<<i<<": "<<nilai<<endl;
	}
}
