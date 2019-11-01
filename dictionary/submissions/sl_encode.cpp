// usage: ./a.out < downloads/dict.txt | bzip2 > submissions/accepted/sl/c
#include <bits/stdc++.h>
using namespace std;

int main() {
	string last, temp, word;
	bool first = true;
	while (getline(cin, word)) {
		if (!first) cout << '%';
		first = false;
		temp = word;
		size_t i;
		for (i = 0; i < min(word.size(), last.size()); i++) {
			if (word[i] != last[i]) break;
		}
		if (word.substr(i) == "'s" && last.substr(i).empty()) ;
		else {
			char prefix = (char)(last.size() - i);
			assert(prefix != '%');
			cout << prefix;
			cout << word.substr(i);
		}
		swap(last, temp);
	}
}
