#include <bits/stdc++.h>
using namespace std;

int main () {
    int t, x, n;
    cin >>t;

    while (t--) {
        int c = 1, ans = 0;
        int a[100000];
        cin >>n>>x;

        for (int i = 0; i < n ;i++) {
            cin >> a[i];
        }
        sort (a, a + n);
       

        for (int i = n - 1; i >= 0;i--) {
            if (a[i] *c >= x) {
                ans++;
                c = 0;
            }
            c++;
        }
        cout<<ans<<endl;
    }
}