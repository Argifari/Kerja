#include <bits/stdc++.h>
using namespace std;


int main () {
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    int n, m;
    
    class Solution {
        public :        
            vector<int> bfsOfGraph (int v, vector<int> adj[]) {
            int n;
            int vis[n] = {0};
            vis[0] = 1;
            queue<int>q;
            vector<int>bfs;
            q.push(0);

            while (!q.empty()) {
                 int node = q.front();
                 q.pop();
                 bfs.push_back(node);

                 for (auto it : adj[node]) {
                    if (!vis[it]) {
                        vis[it] = 1;
                        q.push(it);
                    }
                 }
            }
            return bfs;
        }
    };
   
}       