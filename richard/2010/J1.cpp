#include<iostream>

using namespace std;
int main() {
	int n;
	cin >> n;
	int c = 0;
	int h1;
	int h2;
	if (n > 5) {
		h1 = 5;
		h2 = n - 5;
	} else {
		h1 = n;
		h2 = 0;
	}
	for (int i = 0; i < 5; i++) {
		c ++;
		if (h1 == h2 or h1 - 1 == h2) {
			break;
		} else {
			h1 --;
			h2 ++;
		}
	}
	cout << c;
}

