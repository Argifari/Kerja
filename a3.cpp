#include <iostream>

using namespace std;

int main () {
    int t; 
    cin >> t;

    while (t--) {
        int n,cek = 0;
        cin >> n;

        int a[n];

        for (int i = 0; i < n; i++) {
            cin >>a[i];
        }
        for (int i = 0; i < n; i++) {
            if (a[i] == 1) {
                cek++;
            }
        }
        if (cek == n) {
            if (cek % 2 == 1) {
                cout<<"First"<<endl;
            }else {
                cout<<"Second"<<endl;
            }
        }else {
            for (int i = 0; i < n;i++) {
                if (a[i] != 1) {
                    if ((i + 1 )% 2 == 0) {
                        cout<<"Second"<<endl;
                    }else if ((i + 1) % 2 == 1) {
                        cout<<"First"<<endl;
                    }
                    break;
                }
            }

        }
    }
}