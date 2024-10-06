#include <bits/stdc++.h>

using namespace std;

int main () {
    long long t, n, k;

    cin >> t;
    while (t--) {
        cin >> n >> k;
        long long a[n], b[n],ans[100000];
        bool ngecek[n];
        memset(ngecek, true, sizeof(ngecek));

        for (long long i = 0; i < n; i++) {
            cin >> a[i];
        }for (long long i = 0; i < n; i++) {
            cin >> b[i];
        }
        long long cek;

        for (long long i = 0; i < n; i++) {
            for (long long j = 0; j < n; j++) {
                cek = abs (a[i] - b[j]);
                if (cek <= k) {
                    if (ngecek[j]) {
                        ans[i] = b[j];
                        ngecek[j] = false;
                        break;
                    }
                }
            }
        }
        for (long long i = 0; i < n; i++) {
            cout<<ans[i]<<" ";
        }
        cout<<endl;
    }
}