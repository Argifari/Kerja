#include <bits/stdc++.h>
using namespace std;

int main () {
    int n;
    cin>> n;
    string tamu[n];

    for (int i = 0; i < n ; i++) {
        cin >> tamu[i];
    }
    for (int i = 0; i < n ;i++) {
        for (int j = i +1; j < n; j++) {
            if (tamu[i].size() >tamu[j].size() ) {
                swap(tamu[i],tamu[j]);
            }else if (tamu[i].size() == tamu[j].size()) {
                if (tamu[i] > tamu[j]) {
                    swap (tamu[i] , tamu[j]);
                }
            }
        }
    }
    for (int i = 0;i < n; i++) {
        cout<<tamu[i]<<endl;
    }
}