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
	cin.exceptions(cin.failbit);
	int N, M;
	cin >> N >> M;
	vi cost(N);
	rep(i,0,N) {
		cin >> cost[i];
		assert(cost[i] <= 10);
	}
	int si = 0;
	while (M >= 20 && si < N) {
		M -= cost[si];
		si++;
	}
	if (si == N) {
		cout << 0 << endl;
		return 0;
	}
	int res = INT_MAX;
	rep(m,0,M+1) {
		int have = m, r = 0;
		rep(i,si,N) {
			if (cost[i] > have) r++;
			else have -= cost[i];
		}
		res = min(res, r);
	}
	cout << res << endl;
}
