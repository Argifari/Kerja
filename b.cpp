#include <bits/stdc++.h>

using namespace std;

int main () {
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    queue <long long> v;
    set<long long> st;

    long long q;
    cin >> q;

    while (q--) {
        long long a;
        cin >> a;

        if (a == 1) {
            long long t;
            cin >> t;
            v.push(t);
        }else if (a == 2) {
            
        }else {
            for (int i = 0; i < v.size(); i++) {
                st.insert(v.front());
                v.pop();
            }
        }
    }
}