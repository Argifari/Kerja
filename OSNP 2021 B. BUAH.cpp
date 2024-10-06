#include <bits/stdc++.h>
#define ll long long
using namespace std;

int main () {
	ll N, A, B;
	cin >> N >> A >> B;
	
	ll FPB = __gcd (A, B);
	
	if ((A / FPB) > N ||(B / FPB) > N) {
		cout<< (A / A) + (B / B) <<endl;
	}else {
		cout<< (A / FPB) + (B / FPB)<< endl;
	}
}
