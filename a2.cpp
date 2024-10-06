#include <bits/stdc++.h>
using namespace std;

int main () {
    int t;
    cin>> t;

    while (t--) {
        int n;
       

        cin >> n;
        pair <int ,int> a[n];
        // int a[n];
         int b[n];

        for (int i = 0; i < n; i++) {
            a[i].first = i;
            cin>>b[i];
            a[i].second = b[i];
        }
        sort (a, a + n, [](pair <int,int>a,pair<int,int>b) {
            return a.second < b.second;
        });
        for (int i = 0; i < n;i++) {
            for (int j = n; j >= 0; j--) {
                if (i != a[j].first) {
                    int p = b[i] - a[j].second;
                    cout<<p<<" ";
                    break;
                }
            }
        }

    }
}