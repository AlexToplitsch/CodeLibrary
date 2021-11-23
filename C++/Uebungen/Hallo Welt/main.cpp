#include <iostream>
#include <string>

using namespace std;

int main(int argc, const char* argv[]) {
	for (int year = 2010; year <= 2022; year++) {
		if (year % 4 != 0) {
			cout << year << endl;
		}
		/*if (year == 2016 || year == 2012 || year == 2020) {
			continue;
		}
		cout << year << endl;*/
	}
}