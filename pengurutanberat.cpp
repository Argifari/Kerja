#include <bits/stdc++.h>

using namespace std;

int main () {
    int n;
    cin >> n;
    int berat[n];
    for (int i = 0 ; i < n ; i++) {
        cin>> berat[i];
    }
    int q;
    cin >> q;
    
    for (int i = 0; i < q; i++)  {
        int x, y;
        cin >> x >> y;
        cout<<upper_bound(berat, berat + n, y) - lower_bound(berat, berat + n, x + 1)<<endl;
    }
}