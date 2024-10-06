#include <bits/stdc++.h>
#define ll long long
using namespace std;

int main () {
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
	ll n, m;
    cin >> n >> m;
    ll a[n];
    for (ll i = 0; i < n; i++) {
        cin >> a[i];
    }
    bool dp[n][m + 1];
    dp[0][0] = true;
	for (ll i = 1; i <= m; i++) {
        if (i == a[0]) dp[0][i] = true;
        else dp[0][i] =false;
    }

    for (ll i = 1; i < n ;i++) {
        dp[i][0] = true;

        for (ll j = 1; j  <= m; j++) {
            if (j >= a[i]) {
                dp[i][j] = dp[i - 1][j - a[i]];
            }
            else {
                dp[i][j] = dp[i - 1][j];
            }
        }
    }
    cout<<dp[n - 1][m]<<endl;
}