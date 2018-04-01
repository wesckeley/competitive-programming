#include <cstdio>

#define MAX 60000

void ftUpdate(int* ft, int iI, int iN) {

	while (iI <= iN) {
		ft[iI]++;
		iI += iI & (-iI);
	}

}

int ftQuery(int *ft, int iI) {

	int iAnswer = 0;

	while (iI > 0) {
		iAnswer += ft[iI];
		iI -= iI & (-iI);
	}

	return iAnswer;

}

int main(void) {

	int iN, iI;
	int iData[(MAX + 1)] , ft[(MAX + 1)];
	int iAnswer = 0;
	
	scanf("%d", &iN);

	for (iI = 1; iI <= iN; iI++) {
		scanf("%d", &iData[iI]);
		ft[iI] = 0;
	}

	ft[0] = 0;
	for (iI = iN; iI >= 1; iI--) {
		ftUpdate(ft, iData[iI], iN);
		iAnswer += ftQuery(ft, iData[iI] - 1);
	}

	printf("%d\n", iAnswer);

	return 0;

}