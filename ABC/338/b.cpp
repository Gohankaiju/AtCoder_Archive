#include <bits/stdc++.h>
using namespace std;
#define rep(i,n) for(int i=0; i<n; ++i)
using ll = long long;
using P = pair<int,int>;

int main() {
    string s;
    cin >> s;
    int cnt[128] = {};
    for(char c : s){
        cnt[c]++;
    }
    char ans = 'a';

    for(char c='b'; c <='z'; c++){
        if(cnt[c] > cnt[ans]){
            ans = c;
        }
    }
    cout << ans << endl;

    return 0;
}
