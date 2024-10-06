#include <bits/stdc++.h>
#define ll long long
using namespace std;

int main () {
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
	ll n, m;
	cin >> n >> m;
	ll koin[m], dp[n + 1];
	for (ll i = 0; i < m; i++) {
		cin >> koin[i];
	}
	dp[0] = 0;

	for (ll i = 1; i <= n; i++)  {
		dp[i] = 1e9;
		for (ll j = 0; j < m; j++ ) {
			if (koin[j] <= i) {
				dp[i] = min (dp[i], 1 + dp[i - koin[j]]);
			}
		}
	}
	cout<<dp[n]<<endl;

}