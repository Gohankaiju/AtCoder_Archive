#include <bits/stdc++.h>
using namespace std;
#define rep(i,n) for(int i=0; i<n; ++i)
using ll = long long;
using P = pair<int,int>;

ll  f(ll r, ll m){
    return r/m;
}

int main() {
    ll a, m, l, r;
    cin >> a >> m >> l >> r;
    
    l -= a; r -= a;

    if(l < 0){
        int x = l;`
        l += -x; r += -x;
    }
    cout << r << " " << l << endl;
    cout << f(r, m) - f(l-1, m) << endl;
    return 0;
}
