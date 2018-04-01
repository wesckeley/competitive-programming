#include <cstdio>

int main(void) {

	int iN, iI;
	int iSum = 0;
	int iValue;

	scanf("%d", &iN);

	for (iI = 0; ((iI < iN) && (iSum < 1000000)); iI++) {
		scanf("%d", &iValue);
		iSum += iValue;
	}

	printf("%d\n", iI);

	return 0;

}