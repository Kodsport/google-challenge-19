// usage: ./a.out input_file output_file dir < contestants_output

#include <bits/stdc++.h>
using namespace std;

string output_dir;

[[noreturn]]
void wa(const string& msg) {
	cout << msg << endl;
	ofstream fout2(output_dir + "/teammessage.txt");
	fout2 << msg << endl;
	ofstream fout(output_dir + "/score.txt");
	fout << 0 << flush;
	exit(43);
}

[[noreturn]]
void ac(double score) {
	ofstream fout(output_dir + "/score.txt");
	fout << setprecision(2) << fixed << score << flush;
	exit(42);
}

int main(int argc, char** argv) {
	cin.sync_with_stdio(false);
	cin.tie(NULL);

	if (argc < 4) {
		cout << "not enough arguments" << endl;
		return 1;
	}

	output_dir = argv[3];
	ifstream ans(argv[2]);

	int wlsize = 0, printed = 0, reading = 1;
	string word, word2;
	while (getline(ans, word)) {
		if (reading) {
			if (!getline(cin, word2) || word2.empty()) {
				reading = 0;
			} else if (word != word2) {
				wa("Mismatched word: got " + word2 + ", expected " + word + ".");
			} else {
				printed++;
			}
		}
		wlsize++;
	}

	if (reading && getline(cin, word2) && !word2.empty()) {
		wa("Expected end of file, saw " + word2 + ".");
	}

	if (printed == 0) {
		wa("No output!");
	}

	ac(printed / (double)wlsize * 500);
}
