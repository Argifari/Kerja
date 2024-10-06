#include <bits/stdc++.h>

using namespace std;

int main () {
	ios_base::sync_with_stdio(0);
	cin.tie(0);
	cout.tie(0);
	long long n, d;
	cin >> n >> d;
	long long a[n];
	set<long long>ans;
	for (long long i = 0; i < n; i++) {
		cin >> a[i];
		ans.insert(a[i]);
	}
	long long cek = 0;
	for (long long i = 0; i < ans.size(); i++) {
		if (ans.count(a[i] + d) == 1) {
			cek++;
		}
	}
	cout<<cek<<endl;
}