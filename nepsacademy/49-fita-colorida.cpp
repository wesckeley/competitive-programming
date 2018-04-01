#include <cstdio>

#define MAX 10000

int getMin(int a, int b) {

	return (a < b) ? a : b;

}

int main(void) {

	int iN, iI;
	int iData[(MAX + 1)], iAnswer[(MAX + 1)];
	int iLastZero = -1;

	scanf("%d", &iN);

	for (iI = 0; iI < iN; iI++) {

		scanf("%d", &iData[iI]);

		if (iData[iI] == 0)
			iLastZero = iI;

		(iLastZero == -1) ? iAnswer[iI] = 9 : iAnswer[iI] = getMin(iI - iLastZero, 9);

	}

	for (iI = iLastZero; iI >= 0; iI--) {

		if (iData[iI] == 0)
			iLastZero = iI;
				
		iAnswer[iI] = getMin(iAnswer[iI], iLastZero - iI);

	}

	for (iI = 0; iI < (iN - 1); iI++)
		printf("%d ", iAnswer[iI]);
	printf("%d\n", iAnswer[iI]);

	return 0;

}