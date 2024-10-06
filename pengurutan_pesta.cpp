#include <bits/stdc++.h>
using namespace std;

string tamu;

int main () {
	
	int n;
	cin >> n;
	string a[n];
	
	for (int i = 0; i < n; i++) {
		cin >> a[i];
		tamu = a[i];

		sort (a, a + i + 1);
		for (int j = 0; j <= i; j++) {
			if (a[j] == tamu){ 
				cout<< j + 1<<endl;
			}
		}
	}
}
