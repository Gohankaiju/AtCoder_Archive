#include <bits/stdc++.h>
using namespace std;
#define rep(i,n) for(int i=0; i<n; ++i)
using ll = long long;
using P = pair<int,int>;

int main() {
    string s;
    cin >> s;

    for(int i=0; i<s.size(); i++){
        if(i == s.size()-1) break;
        char c = s[i];
        char nex = s[i+1];
        if(c == 'A'){
            continue;
        }else if(c == 'B'){
            if(nex == 'A'){
                cout << "No" << endl;
                return 0;
            }
        }else{
            if(nex != 'C'){
                cout << "No" << endl;
                return 0;
            }
        }
    }

    cout << "Yes" << endl;

    return 0;
}
