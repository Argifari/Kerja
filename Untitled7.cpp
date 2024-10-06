#include <bits/stdc++.h>
#define ll long long
using namespace std;

int main () {
	ll N, uang;
	
	cin>> N >> uang;
	ll har[N], kan[N];
	bool dos[N];
	ll a[uang + 1];
	
	for (ll i = 0;i<= uang;i++) {
		a[i]= 0;
	}
	for (ll i = 0;i < N;i++){
		cin>> har[i]>>kan[i]>>dos[i];
		
		if (dos[i]==true) {
			for (ll j = uang;j >= har[i];j--) {
				a[j] = max (kan[i]+a[j-har[i]], a[j]);
			}
		}else {
			for (ll j = har[i];j <= uang;j++) {
				a[j] = max (kan[i]+ a[j-har[i]], a[j]);
			}
		}
	}
	cout<<a[uang]<<endl;
	return 0;
}

