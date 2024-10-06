#include <bits/stdc++.h >

using namespace std;

int main () {
    int t ;
    cin >> t;

    while (t--) {
        int n,m,k;

        cin >> n>>m>>k;

        if (n == 1) {
            if (m - 1 == k) {
                cout<<"YES"<<endl;
            }else {
                cout<<"NO"<<endl;
            }
        }else {
            if ((n*m - 1) == k) {
                cout<<"YES"<<endl;
            }
            else {
                cout<<"NO"<<endl;
            }
        }
    }
}