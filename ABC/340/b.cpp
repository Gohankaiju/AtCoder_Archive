#include <bits/stdc++.h>
using namespace std;
#define rep(i,n) for(int i=0; i<n; ++i)
using ll = long long;
using P = pair<int,int>;

int main() {
    int n;
    cin >> n;
    vector<int> vec;
    rep(i, n){
        int a, b;
        cin >> a >> b;
        if(a == 1){
            vec.emplace_back(b);
        }else{
            cout << vec[vec.size()-b] << endl;
        }
    }
    

    return 0;
}
