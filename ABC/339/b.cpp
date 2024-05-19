#include <bits/stdc++.h>
using namespace std;
#define rep(i,n) for(int i=0; i<n; ++i)
using ll = long long;
using P = pair<int,int>;

int main() {
    int h, w, n;
    cin >> h >> w >> n;
    vector<vector<int>> gri(h, vector<int>(w, 0));
    vector<P> dist = {{-1, 0},{0, 1},{1, 0},{0, -1}};
    int muki = 0;
    int now[2] = {0, 0};

    rep(i, n){
        //cout << endl;
        int x, y;
        x = now[0];
        y = now[1];

        if(gri[x][y] == 0){
            gri[x][y] = 1;
            muki = (muki + 1) % 4;

            now[0] = (now[0] + dist[muki].first) % h;
            if(now[0] < 0) now[0] = h-1;

            now[1] = (now[1] + dist[muki].second) % w;   
            if(now[1] < 0) now[1] = w-1;
        }else{
            gri[x][y] = 0;
            muki = (muki + 3) % 4;

            now[0] = (now[0] + dist[muki].first) % h;
            if(now[0] < 0) now[0] = h-1;

            now[1] = (now[1] + dist[muki].second) % w;   
            if(now[1] < 0) now[1] = w-1;
        }
        //cout << "muki=" << muki << endl;
        //cout << now[0] <<" " << now[1] << endl;
    }

    rep(i, h){
        rep(j, w){
            if(gri[i][j] == 0) cout << ".";
            else cout << "#";
        }
        cout << endl;
    }
    return 0;
}
