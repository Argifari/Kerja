#include <bits/stdc++.h>

using namespace std;

int main () {
    int n;
    int q;
    string nama,nomor;

    cin >> n>>q;
    map<string, string> wartel;
    for (int i = 0; i < n; i++) {
        cin >> nama>> nomor;
        wartel[nama] = nomor;
    }
   while (q--) {
    string cek;
    cin >> cek;
    if (wartel.count(cek)) {
        cout<<wartel[cek]<<endl;
    }else {
        cout<<"NIHIL"<<endl;
    }
   }

}