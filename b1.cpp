#include <bits/stdc++.h>
#define ll long long
using namespace std;

int main () {
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    ll n, m;
    cin >> n >> m;
    bool menang[m + 1];
    memset(menang, true, sizeof(menang));
    tuple<string, ll, ll> peserta[n];

    for (ll i = 0; i < n; i++) {
        cin >> get<0>(peserta[i]) >> get<1>(peserta[i]) >> get<2>(peserta[i]);
    }

    sort (peserta, peserta + n, [](tuple <string, ll, ll> a, tuple <string,ll,ll> b)
    {
        return get<1>(a) < get<1>(b) || (get<1>(a) == get<1>(b) && get<2>(a) > get<2>(b));
    } );
    ll rek2 = 0;

    for (ll i = 0; i < n; i++ ) {
        if (m == 0) break;
        if (get<1>(peserta[i + 1]) == get<1>(peserta[i + 2]) && menang[get<1>(peserta[i])]) {
            if (get<2>(peserta[i + 1]) == get<2>(peserta[i + 2])) {
                cout<<"?"<<endl;
                m--;
                menang[get<1>(peserta[i])] = false;
             }else {
                cout<<get<0>(peserta[i])<<" "<<get<0>(peserta[i + 1])<<endl;
                menang[get<1>(peserta[i])] = false;
                m--;
             }
        }
        else if (menang[get<1>(peserta[i])]){
            cout<<get<0>(peserta[i]) <<" "<<get<0>(peserta[i + 1])<<endl;
            menang[get<1>(peserta[i])] = false;
            m--;
        }
        
    }
    
}