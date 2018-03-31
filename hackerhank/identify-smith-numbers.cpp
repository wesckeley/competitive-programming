#include <bitset>
#include <cstdio>
#include <vector>

#define MAX 46341

using namespace std;

int getDigitsSum(int iNumber) {

	int iAnswer = 0;

	while (iNumber > 0) {
		iAnswer += (iNumber % 10);
		iNumber /= 10;
	}

	return iAnswer;

}

int getPrimesDigitsSum(int iNumber, vector< int >& iPrimes) {

	int iAnswer = 0;
	int iI;

	for (iI = 0; ((iNumber > 1) && (iI < iPrimes.size())); iI++) {

		while ((iNumber % iPrimes[iI]) == 0) {

			iAnswer += getDigitsSum(iPrimes[iI]);
			iNumber /= iPrimes[iI];

		}

	}

	if (iNumber > 1)
		iAnswer += getDigitsSum(iNumber);

	return iAnswer;

}

int main(void) {

	int iI, iJ;
	bitset<(MAX + 1) > bPrimes;
	vector< int > iPrimes;
	int iNumber;

	bPrimes.set();

	for (iI = 2; (iI * iI) <= MAX; iI++)
		if (bPrimes[iI] == true)
			for (iJ = (iI * iI); iJ <= MAX; iJ += iI)
				bPrimes[iJ] = false;

	iPrimes.clear();

	for (iI = 2; iI <= MAX; iI++)
		if (bPrimes[iI] == true)
			iPrimes.push_back(iI);

	scanf("%d", &iNumber);

	(getDigitsSum(iNumber) == getPrimesDigitsSum(iNumber, iPrimes)) ? printf("1\n") : printf("0\n");

	return 0;

}