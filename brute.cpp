#include <bits/stdc++.h>
using namespace std;

int main () {
    int n,k;
    double harga = 0;

    cin >> n >> k;
    pair <double, int> a[n];

    for (int i = 0; i < n;i++) {
        cin >> a[i].second;
    }
    for (int i = 0; i < n; i++) {
        cin >> a[i].first;
    }

    for (int i = 0; i < n; i++) {
        a[i].first /= a[i].second; 
    }

    sort (a, a + n,[](pair <double, int>a, pair <double,int>b) {
        return a.first > b.first;
    });
    int cek = 1;
    for (int i = 0; i < n; i++) {
        for (int j = 1; j <= a[i].second; j++) {
            harga += a[i].first;
            k--;
            if (k == 0) {
                break;
            }
        }
        if (k == 0) {
            break;
        }
    }
    cout<<fixed<<setprecision(5)<<harga<<endl;
}