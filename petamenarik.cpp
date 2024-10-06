#include <bits/stdc++.h>

using namespace std;

int main () {

    int N, M,K;

    cin >> N >> M >> K;

    int a[105][105];
   

    for (int i = 1; i <=  N; i++) {
        for (int j = 1; j <= M; j++) {
            cin >>a[i][j];
        }
    }
    bool ans = false;

    for (int j = 1; j <= M; j++) {
        for (int i = 1; i <=N; i++) {
             int cek = 1;
            if ( j - 1 > 0) {
                cek *= a[i][j - 1];
                ans = true;
            }if (j + 1 <= M){
                cek *= a[i][j + 1];
                ans = true;
            }if (i - 1 > 0) {
                cek *= a[i - 1][j];
                ans = true;
            }if (i + 1 <= N) {
                cek *= a[i + 1][j];
                ans = true;
            }
            if (cek == K && ans) {
                cout<<i<< " "<<j<<endl;
                return 0;
            }
        }
    }
    cout<<"0 0"<<endl;
}