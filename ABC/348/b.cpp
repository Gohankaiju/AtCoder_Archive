#include <bits/stdc++.h>
using namespace std;
#define rep(i,n) for(int i=0; i<n; ++i)

int main() {
    int n;
    cin >> n;
    vector<pair<int, int>> ten(n);
    vector<int> ans;
    rep(i, n){
        int a, b;
        cin >> a >> b;
        ten[i] = {a, b};
    }
    //cout << ten[2].first << endl;

    for(auto dot : ten){
        int max = 0, tmp = -1;
        for(int i=0; i<n; i++){
            auto dot2 = ten[i];
            int kyori = pow((dot.first - dot2.first), 2) + pow((dot.second - dot2.second), 2);
            //cout << kyori << endl;
            if(max < kyori){
                max = kyori;
                tmp = i+1;
            }
        }
        ans.emplace_back(tmp);
    }
    
    for(int a : ans)    cout << a << endl;

    return 0;
}
