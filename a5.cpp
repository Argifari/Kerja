#include <bits/stdc++.h>

using namespace std;

int main () {
     int t, k, ans;

     cin >> t >> k;
     deque <int > A, B, C;
     int a,b,c;
     for (int i = 0; i < t; i++) {
   
            cin >>c>>a>>b;

            if (a == 1 && b == 1) {
                C.push_back(c);
            }else if (a==1) {
                A.push_back(c);
            }else if (b == 1) {
                B.push_back(c);
            } 
     }
     sort (A.begin(), A.end());
     sort (B.begin(), B.end());
     sort (C.begin(), C.end());

     while (k--) {

        if ((A.empty() || B.empty()) && C.empty()) {
            ans = -1;
            break;
        }if (C.empty() ||( !A.empty() && !B.empty() && A.front() + B.front() < C.front())) {
            ans += A.front() + B.front();
            A.pop_front();
            B.pop_front();
        }else {
            ans += C.front();
            C.pop_front();
        }
     }
     cout<<ans<<endl;
}