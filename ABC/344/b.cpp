#include <bits/stdc++.h>
using namespace std;
#define rep(i,n) for(int i=0; i<n; ++i)

int main() {
    stack<int> st;

    while(true){
        int x;
        cin >> x;
        if(cin.eof()) break;
        st.push(x);
    }
    int size = st.size();
    rep(i, size){
        int num = st.top();
        cout << num << endl;
        st.pop();
    }

    return 0;
}
