#include <bits/stdc++.h>
#define ll long long
using namespace std;

int main (){
	ll N,jmlhuruf[26];
	string S, huruf = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
	
	cin>> N;
	cin>>S;
	
	memset (jmlhuruf, 0, sizeof (jmlhuruf));
	
	for (ll i = 0;i < N;i++) {
		for (ll j = 0;j < 26;j++) {
			if (S[i]==huruf[j]) {
				jmlhuruf[j]++;
			}
		}
	}
	
	sort (jmlhuruf, jmlhuruf+26,greater<ll>());
	ll ans = 3*jmlhuruf[2];
	
	if (jmlhuruf[2]< 1){
		ans = -1;
	}else {
		if (jmlhuruf[2]<jmlhuruf[0]) {
			ans++;
		}if (jmlhuruf[2]<jmlhuruf[1]) {
			ans++;
		}
	}
	cout<<ans<<endl;
}






