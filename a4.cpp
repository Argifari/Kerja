#include <bits/stdc++.h>

using namespace std;

int main () {
    int t; 
    cin >> t;

    while (t--) {
        int n,cek = 0;
        cin >> n;
        int a[n][2];
        int b[n][2];
        for (int i = 0; i < n; i++) {
            cin >> a[0][i];
        }

        for (int i = 0; i < n; i++) {
            cin >> a[1][i];
        }
        
        for (int i = 1; i < n; i++) {
            a[0][i] += a[0][i - 1];
        }
        //alice ngambil yang maksimal agar bob minimal carilah mimimal poin
    }
}