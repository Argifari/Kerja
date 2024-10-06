#include <bits/stdc++.h>
using namespace std;

int main () {
    int t, n;
    cin >> t;

    while (t--) {
        cin >> n;
        int c = 0, as = 0;

        int a[n] ;

        for (int i = 0; i < n; i++) {
            cin >> a[i];
        }
        for (int i = 0; i < n; i++) {
            if (a[i] == 0 ) {
                c++;
            }
            if (as <= c) {
                as = c;
            }
            if (a[i + 1] == 1) {
                c = 0;
            }
        }
        cout<<as<<endl;
    }
}