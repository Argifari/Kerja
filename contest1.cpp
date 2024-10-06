#include <bits/stdc++.h>
using namespace std;

int main () {
    int t; 
    cin >> t;
    while (t--) {
 
    string s;
    int n, cek = 0, ans = 0, a = 0;
    cin >>n;
    cin >> s;
    bool prime[n + 2];
    memset (prime, true, sizeof(prime));

    for (int i = 1; i < s.length(); i+=2) {
        cek = 0;
        if (prime[i]) {
            cout<<i<<endl;
            prime[i - 1] = false;
            a++;
        for (int j = 0; j < s.length(); j++) {
            if (s[i] == s[j]) {
                if (prime[j]) {
                    //cout<<cek<<endl;
                    //cout<<s[i]<<endl;
                    //cout<<s[j]<<" "<<j<<endl;
                    prime[j + 1] = false; 
                    prime[j] = false;
                    cek++;
                    if (cek > 1) {
                        prime[j] = false;
                        cek = 1;
                        
                    }
                }
            }
        }
    }
        ans += cek;
    }
    cout<<ans + a<<endl;
    }

}