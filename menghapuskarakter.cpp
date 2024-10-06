#include <bits/stdc++.h>

using namespace std;

int main () {

    int n, k;
    cin >> n >> k;
    char a[n];

    for (int i = 0; i < n;i++) {
        cin>>a[i];
    }
    sort(a, a + n);
    cout<<a[k - 1]<<endl;

    // for (int i = 0; i < n; i++ ) {
    //     if (i == k - 1) {
    //         cout<<a[i]<<endl;
    //         break;
    //     }
    // }
}