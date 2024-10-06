#include <bits/stdc++.h>
#define ii long long
using namespace std;

int main () {
	ii cas, n, m, sesi = 0, nilai,b;
	
	cin>>cas;
	
	while (cas--) {
		cin>>n>>m;
		ii a[n];
		
		for (ii i = 0;i < n;i++) {
			cin>>a[i];
		}
		for (ii i = 0;i < n;i++) {
			a[i]+=b;
			if (a[i] >= m) {
				b = m - (a[i]-b);
				continue;
			}
			nilai = m-a[i];
			sesi += nilai;
			b +=nilai;
		}
		cout<<sesi<<endl;
	}
}
