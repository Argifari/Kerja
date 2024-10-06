#include <bits/stdc++.h>
#define ll long long
using namespace std;

int main () {
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    ll tc;
    cin >> tc;
    ll k, tinggi = 0, rendah = 1e10;
    cin >> k;
    ll a[tc];
    for (ll i = 0; i < tc; i++) {
        cin >> a[i];
    }
    sort(a, a + tc);
    for (ll i = 0; i < k; i++) {
        if (i + k -1 > tc) {
            rendah = min (rendah, a[i + k -1] - a[i]);
        }
    }
    cout<<rendah<<endl;
}