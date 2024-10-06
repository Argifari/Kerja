#include <bits/stdc++.h>
using namespace std;

int main () {
    int t;
    cin >> t;

    while (t--) {
        int n,k;
        cin >> n>>k;
        pair <int , int> ram[n];
        for (int i = 0; i < n; i++) {
            cin>>ram[i].first;
        }
         for (int i = 0; i < n; i++) {
            cin>>ram[i].second;
        }
        sort(ram, ram + n,[](pair <int,int> a, pair<int,int>b) {
            return a.first < b.first;
        });
         for (int i = 0; i < n; i++) {
            if (k >= ram[i].first) {
                    k += ram[i].second;
            }      
        }
        cout<<k<<endl;
    }
}