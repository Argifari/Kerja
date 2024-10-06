#include <bits/stdc++.h>
using namespace std;

int cnt[10];              //cnt[i] merupakan jumlah elemen i dari array
int isi[100005];          //isi[i] merupakan isi array
int pref[10][100005];     //pref[i][j] merupakan jumlah elemen i dari 1 hingga j
int ans,maxka,maxki,n;    //maxka merupakan jumlah maksimum elemen di sebelah kanan pointer, maxki sebelah kiri.

int main(){
	cin >> n;
	for(int i = 1;i <= n;i++) {cin >> isi[i]; }               //Membaca input
	for(int i = 1;i <= n;i++){
		cnt[isi[i]]++;                          
		for(int j = 0;j <= 9;j++){
			pref[j][i] = pref[j][i-1];              //Generate prefix
			if(j == isi[i]) pref[j][i]++;
		}
	}	
	for(int i = 1;i <= n;i++){				
		maxka = maxki = 0;				//Maximum dan minimum direset
		for(int j = 0;j <= 9;j++){
			maxki = max(maxki,pref[j][i]);		//Di cek, elemen apa yang di sebelah kirinya paling banyak
			maxka = max(maxka,cnt[j]-pref[j][i]);	//Di cek, elemen apa yang di sebelah kanannya paling banyak
		}
		ans = max(ans,maxka+maxki);			//Penggabungan dua elemen tersebut
	}
	cout << ans << endl;					//Output jawaban
}	





