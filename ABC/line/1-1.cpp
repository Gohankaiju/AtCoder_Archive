#include <iostream>
#include <vector>
#include <cstdlib>
#include <iomanip>

using namespace std;

int count_tiles(int n, int m) {
    int total_tiles = n * m;

    if (total_tiles % 2 != 0) {
        return 0;
    }

    int half_tiles = total_tiles / 2;

    vector<vector<long long>> dp(total_tiles + 1, vector<long long>(half_tiles + 1, 0));
    dp[0][0] = 1;

    for (int i = 1; i <= total_tiles; ++i) {
        for (int j = 0; j <= half_tiles; ++j) {
            dp[i][j] = dp[i - 1][j];
            if (j > 0) {
                dp[i][j] += dp[i - 1][j - 1];
            }
        }
    }

    long long result = dp[total_tiles][half_tiles];

    return result;
}

int main() {
    try {
        int n, m;
        if (!(cin >> n >> m)) {
            throw invalid_argument("Invalid input");
        }

        if (n < 0 || m < 0) {
            throw invalid_argument("n and m must be non-negative");
        }

        int result = count_tiles(n, m);
        cout << result << endl;
        cout << setw(9) << setfill('0') << result << endl;
    } catch (const exception &e) {
        return 100;
    }

    return 0;
}
