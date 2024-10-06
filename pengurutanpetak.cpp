#include <bits/stdc++.h>

using namespace std;


int main () {
    int N, M, K;
    cin >> N >>M >>K;
    int a[N][M], b[N][M];


    for (int i = 0; i < N; i++) {
        for (int j = 0; j < M; j++) {
            cin >> a[i][j] ;
        }
    }
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < M; j++) {
            b[i][j] = a[i][j] * a[i][j + 1]* a[i + 1][j];
        }
    }
}