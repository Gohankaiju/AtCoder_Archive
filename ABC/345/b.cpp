#include <bits/stdc++.h>
using namespace std;
#define rep(i,n) for(int i=0; i<n; ++i)

int main() {
    long long n, amari;
    cin >> n;
    amari = n % 10;

    if(n > 0){
        if(amari == 0){
            cout << n/10;
        }else{
            cout << n/10 + 1;
        }
        cout << endl;
    }else{
        cout << n/10 << endl;
    }
    
    return 0;
}
