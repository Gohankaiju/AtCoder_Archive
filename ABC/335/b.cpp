#include <bits/stdc++.h>
using namespace std;
#define rep(i,n) for(int i=0; i<n; ++i)
using ll = long long;
using P = pair<int,int>;

int main() {
    int n;
    cin >> n;
    rep(i, n+1){
        rep(j, n+1){
            rep(k, n+1){
                if(i + j + k <= n)  cout << i << " " << j << " " << k << endl;
            }
        }
    }
    

    return 0;
}
