#include <bits/stdc++.h>
#define II long long
using namespace std;

int main () {
	II t,c1=0,c2=0;
	
	cin>>t;
	II a;
	
	for (II i=0;i<t;i++) {
		cin>>a;
		for (II j=1;j<=a;j++) {
			c1++;
		      if ((c1+c2)>=a) {
			    cout<<c1<<" "<<c2/2<<endl;
			    c1=0;
			    c2=0;
			    break;
		}c2+=2;
	}c1=0;
	c2=0;
	
}
}
