#include <bits/stdc++.h>
using namespace std;

int main () {
    int t; 
    cin >> t;

    while (t--) {
        int n;
        cin >> n;
        int a[n];
        int cek = 0, cek1 = 0;

        for (int i = 0; i < n; i++) {
            cin >>a[i];
        }
        for (int i = 0;i < n; i++) {
            if (a[i] % 2 == 0) {
                cek += a[i];
            }
            else {
                cek1+= a[i];
            }
        }
        if (cek > cek1) {
            cout<<"YES"<<endl;
        }
        else {
            cout<<"NO"<<endl;
        }
    }
}