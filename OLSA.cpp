#include <bits/stdc++.h>
#define ll long long
using namespace std;

int main () {
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
      ll n, a, b , c ;
      cin >> n >>a>>b>>c;
      ll dp[n + 1], total = 0;
      
      dp[0] = 0;
      for (ll i = 1; i <= n; i++) {
         dp[i] = 0;
         if (i >= a) {
            if(dp[i - a] == 0 && i - a != 0) {
                dp[i] = max(dp[i], dp[0]);
            }
			   else dp[i] = max(dp[i], 1 + dp[i - a]);
		   }
		   if (i >= b) {
            if(dp[i - b] == 0 && i - b != 0) {
                dp[i] = max(dp[i], dp[0]);
            }
			   else dp[i] = max(dp[i], 1 + dp[i - b]);;
		   }
		   if (i >= c) {
            if(dp[i - c] == 0 && i - c != 0) {
                dp[i] = max(dp[i], dp[0]);
            }
			   else dp[i] = max(dp[i], 1 + dp[i - c]);
         }
      }
      cout<<dp[n]<<endl;

    
}