#include <bits/stdc++.h>
using namespace std;

int main () {
    int bilangan = 0;
    for (int i = 1 ; i <= 99; i++) {
        if (i % 2 == 0 && i % 3 != 0) {
            bilangan += i;
        }
    }
    cout<<bilangan<<endl;
}