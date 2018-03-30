#include <cstdio>

#define MAX 100

int gcdStein(int iA, int iB) {

	int iG;

	for (iG = 1; !((iA | iB) & 1); iA >>= 1, iB >>= 1, iG <<= 1);

	while (iA != 0) {

		for (; ((iA & 0x01) == 0x00); iA >>= 1);
		for (; ((iB & 0x01) == 0x00); iB >>= 1);

		if (iA >= iB)
			iA = (iA - iB) >> 1;
		else
			iB = (iB - iA) >> 1;

	}

	return iG * iB;

}

int main(void) {

	int iT, iN, iA[MAX], iI;
	bool bAnswer;
	int iGcd;

	scanf("%d", &iT);

	for (; iT > 0; iT--) {

		scanf("%d", &iN);

		for (iI = 0; iI < iN; iI++)
			scanf("%d", &iA[iI]);

		if (iN == 1)
			bAnswer = (iA[0] == 1);
		else {

			iGcd = gcdStein(iA[0], iA[1]);
			for (iI = 2; iI < iN; iI++)
				iGcd = gcdStein(iGcd, iA[iI]);

			bAnswer = (iGcd == 1);

		}

		(bAnswer == true) ? printf("YES\n") : printf("NO\n");

	}

	return 0;

}