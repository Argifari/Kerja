#include <bits/stdc++.h>
using namespace std;

int main () {

    int t, n; 
    
    bool prime[1000000];
    vector<int>ans;

    memset(prime, true, sizeof(prime));

    for (int i = 2; i < 1000000; i++) {
        if (prime[i]) {
            ans.push_back(i);

            for (int j = i*2; j < 1000000; j+=i) {
                prime[j] = false;
            }
        }
    }
    cin >> t;
    for (int i = 0; i < t; i++) {
        cin >> n;
        cout<< ans[n - 1]<<endl;
    }
}