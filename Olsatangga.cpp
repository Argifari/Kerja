#include <bits/stdc++.h>
#define II long long
using namespace std;

int main () {
	int x, y,z,t1,t2,t3;
	cin>>x>>y>>z>>t1>>t2>>t3;
	
	int tangga=t1*abs(x-y);
	int elevator=3*t3+t2*abs(x-y)+t2*abs(x-z);
	
	if (tangga<elevator) cout<<"NO"<<endl;
	else cout<<"YES"<<endl;
}
