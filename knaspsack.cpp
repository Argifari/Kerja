#include <bits/stdc++.h>
#define ll long long
using namespace std;

int main () {
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
	ll n, m;
	cin >> n >> m;
	ll berat[m],value[m], dp[n + 1];
	for (ll i = 0; i < m; i++) {
		cin >> value[i] >> berat[i];
	}
	dp[0] = 0;

	for (ll i = 1; i <= n; i++)  {
		dp[i] = 0;
		for (ll j = 0; j < m; j++ ) {
			if (berat[j] <= i) {
				dp[i] = max(dp[i], value[j] + dp[i - berat[j]]);
			}
		}
	}
	cout<<dp[n]<<endl;

}