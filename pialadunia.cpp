#include <bits/stdc++.h>
using namespace std;
int a[5], b[5];
int n, t;


bool tanding (int tim1, int tim2) {
    if (tim1 == n - 1 && tim2 == n) {
        for (int i = 0; i < n; i++) {
            if (a[i] != b[i]) {
                return false;
            }
        }
        return true;
    }
    else if (tim2 > n - 1) {
        return tanding (tim1 + 1, tim1 + 2);
    }else {

        b[tim1] += 3;
        if (tanding(tim1, tim2 + 1)) {
            return true;
        }
        b[tim1] -= 3;

        b[tim1] += 1;
        b[tim2] += 1;
        if (tanding(tim1, tim2 + 1)) {
            return true;
        }
        b[tim1] -= 1;
        b[tim2] -= 1;

        b[tim2] += 3;
        if (tanding(tim1, tim2 + 1)) {
            return true;
        }
        b[tim2] -= 3;
        return false;
    }
}


int main () {
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    

    cin >> t;
    while (t--) {
        cin >> n;
        for (int i = 0; i < n; i++) {
            cin >> a[i];
        }

        memset(b, 0, sizeof(b));

        if (tanding(0, 1)) {
            cout<<"YES"<<endl;
        }else {
            cout<<"NO"<<endl;
        }
    }

}
