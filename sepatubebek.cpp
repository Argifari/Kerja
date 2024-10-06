#include <bits/stdc++.h>

using namespace std;

int main () {
    int n, m;

    cin >> n >> m;

    long long a[n], b[m];

    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }
    for (int i = 0; i < m; i++) {
        cin >> b[i];
    }

    sort (a, a + n,greater<long long>());
    sort (b, b + m, greater<long long>());

    bool pantat[m];
    memset(pantat, true, sizeof(pantat));
    int cek = 0;

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            if ((a[i] == b[j] ||(a[i] + 1) == b[j])) {
                if (pantat[j]) {
                    cek++;
                    pantat[j] = false;
                    break;
                }
            }
        }
    }
    cout<<cek<<endl;

}