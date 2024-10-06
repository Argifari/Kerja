#include <bits/stdc++.h>
using namespace std;

int main () {
    int t;
    cin >> t;

    while (t--) {
        string a;
        int cek = 0;
        cin >> a;
        string b = a;

        for  (int i = 0; i < a.length()/2 - 1; i++) {
            swap (a[i], a[i + 1]);
            if (a[i] != b[i]) {
                cek++;
                break;
            }
        }
        if (cek == 1) {
            cout<<"YES"<<endl;
        }else {
            cout<<"NO"<<endl;
        }

    }
}