#include <bits/stdc++.h>
using namespace std;
#define rep(i,n) for(int i=0; i<n; ++i)

int main() {
    string s;
    map <char, int> mp;
    cin >> s;
    for(char c : s){
        if(mp.find(c) == mp.end()){
            mp[c] = 1;
        }else{
            mp[c]++;
        }
    }
    vector<int> ans(500, 0);
    for(auto it = mp.begin(); it != mp.end(); it++){
        //cout << it->first << " " << it->second << endl;
        ans[it->second]++;
    } 
    for(auto n : ans){
        if(!(n == 0 || n == 2)){
            cout << "No" << endl;
            return 0;
        }
    }
    cout << "Yes" << endl;

    return 0;
}
