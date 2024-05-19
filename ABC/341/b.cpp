#include <bits/stdc++.h>
using namespace std;
#define rep(i,n) for(int i=0; i<n; ++i)
using ll = long long;
using P = pair<ll,ll>;

int main() {
    int n;
    cin >> n;
    vector<ll> coin(n);
    rep(i, n)   cin >> coin[i];
    vector<P> ex(n-1);
    rep(i, n-1){
        int a, b;
        cin >> a >> b;
        ex[i] = {a, b};
    }

    for(int i=0; i<n-1; i++){
        ll can;
        can = coin[i] / ex[i].first;
        coin[i+1] += can * ex[i].second;
        //cout << "coin = " << coin[i+1] << endl;
    }
    
    cout << coin[n-1] << endl;

    return 0;
}
