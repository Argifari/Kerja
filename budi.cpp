#include <bits/stdc++.h>
using namespace std;

int main () {
	int t, n = 2, k [10000000];
	bool saring [1000000];
	int prime [100000];

	cin >> t;

	for (int i = 0; i < t; i++) {
		cin >> k[i];
	}
	prime [1] = 2;
	for (int i = 2; i < 1000000; i += 2) {
		saring[i] = false;
		saring[i + 1] = true;
	}
	for (int i = 3; i < 1000000; i ++) {
		if (saring[i]) {
			prime [n] = i;
			n ++;

			for (int j = i; j < 1000000; j ++) {
				saring [i*j] = false;
			}
		}
	}
	for (int i = 0; i < t; i++) {
		cout<< prime[k[i]] << endl;
	}
}