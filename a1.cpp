#include <bits/stdc++.h>
#define ll long long
using namespace std;

int main () {
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    ll tc ;
    cin >> tc;

    while (tc--) {
        ll n, m;
        cin >> n >> m;
        ll a[m];
        vector<ll>sehat;

        for (ll i = 0; i < m; i++ ) {
            cin >> a[i];
        }
        sort (a, a + m);

        for (ll i = 0; i < m; i++ ) {
            if (i < m - 1) {
                sehat.push_back(a[i + 1] - a[i] - 1);
            } else {
                sehat.push_back(n - a[i] + a[0] - 1);
            }
        }
        sort(sehat.begin(), sehat.end(),greater<ll>());
        ll cek = 0;

        for (ll i = 0; i < sehat.size(); i++) {
            sehat[i] -= 4*i;
            if (sehat[i] > 0 && sehat[i] != 1) {
                cek += sehat[i] - 1;
            }if (sehat[i]== 1) {
                cek += sehat[i];
            }
        }
        cout<<n - cek <<endl;

    }
}