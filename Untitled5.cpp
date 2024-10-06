#include <bits/stdc++.h>
#define ll long long
using namespace std;
 int min = -1e9;
int main() {
	ll n;
   // Your code goes here
   while (true) {
   	cin>>n;
   	
   	if (n==0) break;
   	
   	ll a[n];
   	
   	for (ll i = 0 ; i < n ;i++) {
   		cin>>a[i];
	   }
	    ll maxSum = -1e9;
        ll i=0;
     for(; i < n ; i++) {
        ll currSum = 0;
        ll j=i;
          for (; j < n ; j++) {
            currSum += a[j];
             if (currSum > maxSum) {
               maxSum = currSum;
     } if (currSum < 0 ) {
     	currSum = 0;
	 }
	 
   }
 }if (maxSum >= 0 ) {
	 	cout<<"The winning streak is "<<maxSum<<endl;
	 }else {
	 	cout<<"Losing streak"<<endl;
	 }
	   
   } 
   return 0;
}
