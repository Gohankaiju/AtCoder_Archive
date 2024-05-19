#include <bits/stdc++.h>
using namespace std;
#define rep(i,n) for(int i=0; i<n; ++i)
using ll = long long;
using P = pair<int,int>;

int main() {
    int n;
    cin >> n;
    vector<int> retu(n);
    rep(i, n)   cin >> retu[i];
    cin >> n;
    vector<int> q(n+1, 0);
    rep(i, n) q[retu[i+1]] =  i;
    rep(i, n+1) cout << q[i] << " ";
    cout << endl;
    
    for(int i=0; i<n; i++){
        int a, b;
        cin >> a >> b;
        if(q[a] < q[b]){
            cout << a << endl;
        }else{
            cout << b << endl;
        }
    }

    return 0;
}
