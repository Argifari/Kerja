#include <bits/stdc++.h>
#define ll long long
using namespace std;

int main () {
	ll N, K;
	cin>> N>> K;
	
	ll patok[N+1],bebek[K+1];
	
	for (ll i = 0;i < N;i++) {
		cin>> patok[i];
	}
	for (ll i = 0;i < K;i++) {
		cin>> bebek[i];
	}
	ll cek,ans;
	
	for (ll i = 0;i < K;i++) {
		cek=0;
		ans=0;
		for (ll j = 0;j < N;j++) {
			cek+=patok[j];
			
			if (bebek[i]>=cek) {
				ans = j+ 1;
			}else {
				break;
			}
		}
		cout<<ans<<endl;
	}
}
