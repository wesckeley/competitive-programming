#include <cstdio>

int getMax(int iA, int iB) {

	return (iA > iB) ? iA : iB;

}

int getMin(int iA, int iB) {

	return (iA < iB) ? iA : iB;

}

int getComb(int iM, int iN) {

	int iMin, iMax;

	iMin = getMax(1, iN - iM);
	iMax = iN - iMin;

	return getMax(0, iMax - iMin + 1);

}

int main(void) {

	int iN, iM;
	int iI;
	long long int iAnswer = 0;

	scanf("%d %d", &iN, &iM);

	for (iI = getMax(1, iN - iM - iM); iI <= iM; iI++)
		iAnswer += getComb(iM, iN - iI);

	printf("%lld\n", iAnswer);

	return 0;

}