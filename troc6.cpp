#include <bits/stdc++.h>

using namespace std;

int main () {
    int n, x, y;
    cin >> n >> x >> y;

    for (int i = 0; i <= n; i++) {
        for (int j = 0; j <= n; j++) {
            for (int k = 0; k <= n; k++) {
                for (int l = 0; l <= n; l++) {
                    if (i + j + k + l == n && i - k == y && j - l == x) {
                        cout<<i<<" "<<j<<" "<<k<<" "<<l<<endl;
                        return 0;
                    }
                }
            }
        }
    }
    cout<<"-1"<<endl;
}