#include <bits/stdc++.h>
using namespace std;
#define rep(i,n) for(int i=0; i<n; ++i)
using ll = long long;
using P = pair<int,int>;

int main() {
    int n;
    vector<int> bina;
    cin >> n;
    int ans = 0;
    
    while(n % 2 == 0){
        ans++;
        n /= 2;
    }

    cout << ans << endl;
    return 0;
}
