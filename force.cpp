#include <bits/stdc++.h>
using namespace std;

int main () {
    int n;
    bool cek = true;
    cin >> n >> n;
    int a[76][76];
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            cin >> a[i][j];
        }
    }
    cin >> n >> n;
    int b[76][76];
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            cin >> b[i][j];
        }
    }
    //identik
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if (a[i][j] != b[i][j]) {
                cek = false;
            }
        }
    }
    if (cek) {
        cout<<"identik"<<endl;
        return 0;
    }
    cek = true;

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if (a[i][j] != b[n - 1 - i][j]) {
                cek = false;
            }
        }
    }
    if (cek) {
        cout<<"horisontal"<<endl;
        return 0;
    }
    cek = true;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if (a[i][j] != b[i][n - 1 - j]) {
                cek = false;
            }
        }
    }
    if (cek) {
        cout<<"vertikal"<<endl;
        return 0;
    }
    cek = true;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if (a[i][j] != b[j][i]) {
                cek = false;
            }
        }
    }
    if (cek) {
        cout<<"diagonal kanan bawah"<<endl;
        return 0;
    }
    cek = true;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if (a[i][j] != b[n - 1 - j][n - 1 - i]) {
                cek = false;
            }
        }
    }
    if (cek) {
        cout<<"diagonal kiri bawah"<<endl;
        return 0;
    }

    cout<<"tidak identik"<<endl;


}