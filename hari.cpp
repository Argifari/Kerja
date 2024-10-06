#include <bits/stdc++.h> 
using namespace std;


	
	int kursi (int n) {
		if (n < 1) return 0;
		else return n + kursi (n - 1);
	}
	
	int re (int top) {
		
		if (top < 1)return 0;
		else return re (top - 1) + kursi (top);
	}
	
	int main () {
		cout << re(10);
	}

