#include <bits/stdc++.h>

using namespace std;

int main () {
    long long n, uang, bebek = 0, harga = 0, cek = 0;
    cin >> n >> uang;

    pair < long long, long long > coklat[n];

    for (long long i = 0; i < n; i++) {
        cin >> coklat[i].first >> coklat[i].second;
    }
    sort (coklat , coklat + n);

    for (long long i = 0; i < n; i++) {
        for (long long j = 0; j < coklat[i].second; j++) {
            harga +=coklat[i].first;
            bebek++;
            if (harga > uang) {
                bebek--;
                cek = 1;
                break;
            }
        }
        if ( cek == 1) {
            break;
        }
    }
    cout<<bebek<<endl;

}