#include <bits/stdc++.h>

using namespace std;

int main () {
    int k, n , q;
    cin >>n >> k>> q;
    pair <long long, long long> a[n];

    for (int i = 0; i < n; i++) {
        cin >> a[i].first;
        a[i].second = i;
    }
    sort (a, a+ n);
    priority_queue<pair <long long, long long>> pq;
    int ans[n];

    for (int i = 0, j = 0; i < n; i++) {
        while (j < n && a[j].first - a[i].first <= k) j++;
        j--;
        pq.push({j - i + 1, j});

        while (!pq.empty() && pq.top().second < i) pq.pop(); 
        ans[a[i].second] = pq.top().first;
    }

    while (q--) {
        int bebek;
        cin >> bebek;

        cout<<ans[bebek - 1]<<endl;
    }

}