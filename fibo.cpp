#include <bits/stdc++.h>

using namespace std;

int main () {

    int t;
    cin >> t;

    while (t--) {

        int n, l ,r , cek = 1 ;

        cin >> n>> l>>r;
        int a[100000];
        a[1] = l;

        for (int i = 2; i <= n; i++) {
            if (l % i == 0) {
                a[i] = l;
                cek++;
            } else {
                int j = l / i;
                j = (j + 1)* i;
                if (j <= r) {
                    a[i] = j;
                    cek++;
                }
            }
        }
        if (cek == n) {
            cout<<"YES"<<endl;
            for (int i = 1; i <= n; i++) {
                cout<<a[i]<<" ";
            }cout<<endl;
        }else {
            cout<<"NO"<<endl;
        }
    }
}