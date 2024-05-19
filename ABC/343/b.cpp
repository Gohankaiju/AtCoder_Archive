#include <bits/stdc++.h>
using namespace std;
#define rep(i,n) for(int i=0; i<n; ++i)

int main() {
    int n;
    cin >> n;
    vector<vector<int>> ans(n);
    rep(i, n){
        rep(j, n){
            int a;
            cin >> a;
            if(a == 1){
                ans[i].push_back(j+1);
            }
        }
    }
    rep(i, (int)ans.size()){
        for(int x : ans[i]){
            cout << x << " ";
        }
        cout << endl;
    }
    return 0;
}
