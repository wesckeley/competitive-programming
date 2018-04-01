#include <cstdio>

#define MAX 5000

using namespace std;

const int iNotes[7] = { 0, 2, 5, 10, 20, 50, 100 };

int getMax(int iA, int iB) {

	return (iA > iB) ? iA : iB;
}

int main(void) {

	int iSum, iCount[7];
	int iI, iJ, iK, iValue;
	int dp[7][(MAX + 1)];

	scanf("%d", &iSum);

	for (iI = 1; iI <= 6; iI++)
		scanf("%d", &iCount[iI]);

	for (iI = 0; iI <= iSum; iI++)
		dp[0][iI] = 0;
	dp[0][0] = 1;

	for (iI = 1; iI <= 6; iI++) {

		iValue = iNotes[iI];

		for (iJ = 0; iJ <= iSum; iJ++)
			dp[iI][iJ] = dp[(iI - 1)][iJ];


		for (iJ = 0; iJ < iCount[iI]; iJ++, iValue += iNotes[iI]) {

			for (iK = iValue; iK <= iSum; iK++)
				dp[iI][iK] += dp[(iI - 1)][(iK - iValue)];

		}

	}

	printf("%d\n", dp[6][iSum]);

	return 0;

}