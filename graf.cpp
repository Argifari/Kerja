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
    int N, ans = 0;
    cin >> N;
    int a[N + 1][N + 1];
    vector <tuple<int, int, int> > edge_list;
    for (int i = 0; i < N; i++) {
        for (int j = 0; j <= N; j++) {
            cin >> a[i][j];
        }
    }
    for (int i = 0; i <= N; i++) {
        for (int j = 0; j <= N; j++) {
            edge_list.push_back(make_tuple(i, j, a[i][j]));
        }
    }
    sort(edge_list.begin(), edge_list.end(), [](tuple<int,int,int> a, tuple<int,int,int>b) 
    {
        return get<2>(a) < get<2>(b) ;
    });
    for (int i = 0; i < N; i++) {
        sets[i] = i;
    }
    for (int i = 0; i < edge_list.size();i++) {
        if (find(get<0>(edge_list[i])) != find(get<1>(edge_list[i]))) {
            joint(get<0>(edge_list[i]), get<1>(edge_list[i]));
            ans+= get<2>(edge_list[i]);
        }
    }
    cout<<ans<<endl; 

}