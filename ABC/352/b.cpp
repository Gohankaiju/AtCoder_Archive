#include <bits/stdc++.h>
using namespace std;
#define rep(i,n) for(int i=0; i<n; ++i)

int main() {
    string a, b;
    vector<int> ans;
    cin >> a >> b;
    int j = 0, n = b.length();
    for(int i=0; i<n; i++){
        if(a[j] != b[i]){
            continue;
        }else{
            j++;
            ans.emplace_back(i+1);
        }
        if(j+1 > a.length())     break;
    }
    
    for(auto a : ans)   cout << a << " ";
    cout << endl;

    return 0;
}
