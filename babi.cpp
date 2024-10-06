#include<bits/stdc++.h>
using namespace std;

int main () {
	//vektor
	//set
	//map
	//stack
	//queue
	
//	int a [10];
	//vektor: dynamic array 
	
	/*vector <int> v;
	v.push_back(5);
	v.push_back(10);
	v.push_back(15);
	
	v.pop_back();
	cout<<v.size()<<" " <<endl;
	
	for (int i=0;i <v.size();i++) {
		cout<<v[i]<<" ";
	}*/
	
	//set 
//	set <int> st;//masukkan elemen
	//ngecek suatu data apakah sudah diterima 
	
//	st.insert (5);
//	st.insert(10);
//	st.insert(15);
	
	//st.count(); //menghitung banyak yang ada di dalamnya 
	
//	cout<<"st.size = "<<st.size()<<endl<<st.count(10)<<endl;
//	cout<<st.count (20)<<endl;
	
	//hapus elemen 
//	st.erase(5);
//	cout<<"st.size = "<<st.size()<<endl;
	//set buat ngurutin array ;
	
//	for (auto elemen :st ) {
//		cout<<elemen<<" ";
//	}
	
	//multi set
//	multiset<int> multia;
//	for (int i =0;i <)
	
	//map
	
	//index nya gak harus angka bisa karakter atau string kiri =key kanan = nilai
	
//	map<string, string> kota;
	
//	kota ["sakti"] = "jogja";
//	kota ["vincent"]="pasuruan";
//	kota ["nugi"] ="semarang";
	
//	cout<<kota["sakti"]<<endl<<kota["vincent"]<<endl;
	
//	map<char, int> frq;
	
//	string s= "olimpiade sains indonesia";
	
//	for (int i=0 ;i <s.length() ;i++) {
//		frq (s(i))++;
//	}for ()


	//stack =mebuka layaknya sebuah tumpukan queue= laayaknya sebuah antrean 
	
//	stack<int> sta;
//	queue <int> que;
//	
//	int a [] ={4, 5 , 10, 12 , 1};
//	//insert elemen
//	
//	for (int i=0;i<5;i++) {
//		sta.push(a[i]);
//	}for (int i=0;i<5;i++) {
//		que.push(a[i]);
//	}
//	cout<<sta.size()<<endl;
//	cout<<"Stack = "<<endl;
//	while (sta.empty()==false) {//baca elemen teratas
//		cout<<sta.top()<<endl;//keluarkan elemen teratas
//		sta.pop();
//	}
//	cout<<endl;
//	cout<<que.size()<<endl;
//	cout<<"Queue = "<<endl;
//	while (que.empty()==false) {//baca elemen terdepan
//		cout<<que.front()<<endl;
//		que.pop();
//	}
}

//kompleksitas
//waktu dan ruang //biasanya paling sensitiv waktu 
//notasi big O > O (sebuah fungsi /variabel)
//i detik = 10 pangkat 8 operasi melebehi kena time limit
// cek pake worst case ya liat batasan pada soal 


// kelas kompleksitas
//-konstan = O(1) konstan input nya berubah namun operasi nya konstan seperti operasi matematika 

//-logaritmik = O(log n) operasi nya lebih cepat dari linear contohnya FPB  O(max(a,b)), memasukkan ke map atau set, 

//-linear = O(n) banyak operasi mengikuti banyaknya n contohnya adalah melakukan sebanyak loop n , menghapus elemen vektor, menaruh elemen 
                 //pada vektor tidak pada ujungnya
//-polinomial= O (n^K) bisa lebih cepat dari linear , contohnya looping di dalam looping 

//-eksponensial= O(2^n) paling lambar contohnya suruh mendaftarkan sub himpnan, banyaknya node pada binary tree (setiap ortu punya 2 anak )
                 //jika n=27 atau 30 sudah melebihi 10^8
//case terburuk haru kurang dari 10^8















