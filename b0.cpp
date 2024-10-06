#include <bits/stdc++.h>

using namespace std;
int n, m;
int j[10005];
int cek = 0;
int ans[10005];
int an;
void grup (int a) {
    cek = 1;
    for (int i = a; i <= m; i+= a) {
        ans[cek - 1] = j[i - 1] + 1;
        if (cek == n - 1){
            an = i;
            break;
        }
        cek++;
    }if (abs((m - an) - a )<= 1) {
        // cout<<"fukyuuuu "<<a<<endl;
        for (int i = 0; i < n - 1; i++) {
            cout<<ans[i]<<" ";
        }
    }else {
        grup(a + 1);
    }
}

int main () {
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    cin >> m;
    
    for (int i = 0; i < m; i++) {
         cin >> j[i];
    }
    cin >> n;

    sort (j, j + m);
    int p = m / n ;
    // cin >> p;
    grup (p);
    
    // for (int i = 0; i <= m; i+= p) {
    //     if (cek == n - 1){
    //         an = i;
    //         break;
    //     }
    //     cek++;
    // }

    // if (grup(p)) {
    //     cout<<"YES"<<endl;
    // }else {
    //     cout<<"fuck you";
    // }
}