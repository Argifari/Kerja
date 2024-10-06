#include <bits/stdc++.h>
#define ll long long
using namespace std;
ll n;
// ll ubin (ll a) {
// 	if (a <= 1) {
// 		return 1;
// 	}
// 	if (a >= 4) {
// 		return( 2*ubin (a - 4) + 2*ubin (a - 3) + 2*ubin (a - 2));
// 	}
// 	else if (a >= 3) {
// 		return (2*ubin (a - 3).\a + 2*ubin (a - 2));
// 	}
// 	else if (a >= 2) {
// 		return (2*ubin (a - 2));
// 	}

// }

int main () {
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
	cin >> n;
	ll dp[n + 1];
	dp[0] = 1;
	
	for (ll i = 1; i <= n; i++) {
		dp[i] = 0;
		if (i >= 4) {
			dp[i] += dp[i - 4];
		}
		 if (i >= 3) {
			dp[i] += 2*dp[i - 3];
		}
		 if (i >= 2) {
			dp[i] += dp[i - 2];
		}if (i >= 1) {
			dp[i] += dp[i - 1];
		}
	
}
	cout<<dp[n]<<endl;
}