#include <bits/stdc++.h> 
using namespace std;
int budi;
int ayam;
int arr[10];

int prima (int ayam) {
    int t= 1;
    arr[1] = 2;
    for (int i = 3; i <= 10 ; i++) {
        
        int p = 1;
        for (int j = 2; j < i; j++) {
             
            if (i % j != 0) {
                p++;
            }if (p == i -1) {
                t++;
                arr[t] = i ;
                break;
            }
            
        }
    }
    cout<<arr[ayam];
}

int main () {
    cin >> budi;
    for (int i = 1; i <= budi; i++) {
        cin>>ayam;
        prima(ayam);
    }
}


