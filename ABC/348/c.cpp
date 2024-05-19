#include <bits/stdc++.h>
using namespace std;
#define rep(i,n) for(int i=0; i<n; ++i)
using ll = long long;
using P = pair<int,int>;

int main() {
    int n;
    cin >> n;
    map<int, int> bean;
    rep(i, n){
        int a;   
        int col;
        cin >> a >> col;
        if(bean.find(col) == bean.end()){
            bean[col] = a;
        }else{
            if(bean[col] > a){
                bean[col] = a;
            }
        }
    }
    //cout << bean[1] << endl;
    int max = 0;
    for(const auto& pair : bean){
        if(max < pair.second){
            max = pair.second;
        }
    }
    cout << max << endl;

    return 0;
}
