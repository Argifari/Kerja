#include <bits/stdc++.h>

using namespace std;
int sets[100000];
int find (int i) {
    if (sets[i] == i) {
        return i;
    }
    else {
        sets[i] = find(sets[i]);
        return find(sets[i]);
    }
}

void joint (int i, int j) {
    int u = find(i), v = find(j);
    if (u != v) {
      if (u < v) {
        sets[u] = v;
      }else {
        sets[v] = u;
      }
    }
    
}

int main () {
    int N, Q;
    cin >>N>>Q;

    for (int i = 0; i < N; i++) {
        sets[i] = i;
    }
    for (int i = 0; i < Q; i++) {
        int c, a, b;

        cin >> c>> a>> b;

        if (c == 1) {
            joint(a - 1, b - 1);
        }
        else{
            if (find(a - 1) == find(b -1)) {
                cout<<"Y"<<endl;
            }else {
                cout<<"T"<<endl;
            }
        }
    }
}