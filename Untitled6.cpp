#include <bits/stdc++.h>
#define ll long long
using namespace std;

int main () {
	ll n;
	
	while (true) {
		cin>>n;
		
		if (n==0) break;
		ll a[n];
		
		for (ll i=0;i < n ;i++) {
			cin>>a[i];
		}
		
		ll maxsum = -1e9;
		ll currentsum = 0;
		
		for (ll i = 0;i < n ;i++) {
			currentsum += a[i];
		}
		
		if (currentsum > maxsum) {
			maxsum = currentsum;
		}if (currentsum < 0) {
			currentsum = 0;
		}
		
		if (maxsum > 0 ) {
			cout<<"The maximum winning streak is "<<maxsum<<endl;
		}else {
			cout<<"Losing streak"<<endl;
		}
	}
}
