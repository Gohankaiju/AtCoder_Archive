#include <bits/stdc++.h>
using namespace std;
#define rep(i,n) for(int i=0; i<n; ++i)

int main() {
    string s = "wbwbwwbwbwbw";
    
    int w, b;
    cin >> w >> b;
    for(int i=0; i< (int)s.size(); i++){
        int cw=0, cb=0;
        for(int j=0; j<w+b; j++){
            if(s[(i+j) % s.size()] == 'w'){
                cw++;
            }else{
                cb++;
            }
        }
        if(cw == w && cb == b){
            cout << "Yes" << endl;
            return 0;
        }
    }

    cout << "No" << endl;
    return 0;
}
