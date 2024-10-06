#include <bits/stdc++.h> 
using namespace std;

int main () {
    int n,t;

    cin >> t;

    while (t--) {
        cin >> n;

        int a = 1;
        int b = n -1;

        for (int i = 2; i*i <= n; i++) {
            if (n % i == 0) {
                a = n/i;
                b = n - (n/i);
                break;
            }
        }
        cout<<a<<" "<<b<<endl;
    }
}