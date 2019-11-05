#include <bits/stdc++.h>
using namespace std;

#define rep(i, from, to) for (int i = from; i < (to); ++i)
#define trav(a, x) for (auto& a : x)
#define all(x) x.begin(), x.end()
#define sz(x) (int)(x).size()
typedef long long ll;
typedef pair<int, int> pii;
typedef vector<int> vi;

int main() {
	cin.sync_with_stdio(false);
	int N, M;
	cin >> N >> M;
	vi cost(N);
	rep(i,0,N) cin >> cost[i];
	int res = INT_MAX;
	for (int m = M-9; m <= M; m++) {
		int have = m, r = 0;
		rep(i,0,N) {
			if (cost[i] > have) r++;
			else have -= cost[i];
		}
		res = min(res, r);
	}
	cout << res << endl;
}
