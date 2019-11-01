#include "validator.h"

void run() {
	int n = Int(1, Arg("n"));
	Space();
	int m = Int(1, Arg("m"));
	Endl();
	SpacedInts(n, 1, 10);
}
