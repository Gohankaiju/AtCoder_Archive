#include <bits/stdc++.h>
using namespace std;
#define rep(i,n) for(int i=0; i<n; ++i)

int main() {
    string s;
    cin >> s;
    int n = s.size();
    set<string> partial;

    for(int i=0; i<n; i++){
        for(int j=0; j<n-i; j++){
            partial.insert(s.substr(i, j+1));
        }
    }
    cout << partial.size() << endl;

    return 0;
}
