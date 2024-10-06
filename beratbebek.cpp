#include <bits/stdc++.h>

using namespace std;

int main () {
    int k, n;

    cin >> k;

    pair <int, long long> a[k];

    for (int i = 0; i < k; i++) {
        cin >> a[i].first;
    }
    for (int i = 0; i < k; i++) {
        cin >> a[i].second;
    }
    cin >> n;
    long long b[n];

    for (int i = 0; i < n; i++) {
        cin>>b[i];
    }

    sort (a, a + k,[](pair <int, int>a, pair <int,int>b){
        return a.second < b.second;
    });

    sort (b, b + n, greater <int>());
    long long harga = 0;
    int cek = 0;
    for (int i = 0; i < n; i++) {
        harga += b[i]*a[cek].second;
        a[cek].first--;
        if (a[cek].first == 0) cek++;
    }

    cout<<harga<<endl;

}