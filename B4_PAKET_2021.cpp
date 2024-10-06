#include <bits/stdc++.h>
#define ll long long
using namespace std;

int main () {
	ll N,x;
	set<ll>a;
	cin>>N;
	
	for (ll i = 1;i <= N; i++) {
		cin>>x;
		
		if (a.lower_bound(x) == a.end()) {
			a.insert(x);
		}else {
			a.erase(a.lower_bound(x));
			a.insert(x);
		}
	}
	cout<<a.size()<<endl;
}
