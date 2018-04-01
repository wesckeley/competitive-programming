#include <algorithm>
#include <cstdio>

#define MAX 100000

using namespace std;

int main(void) {

	int iN, iB;
	int iI, iJ;
	int iData[MAX];
	int iAnswer = 0;

	scanf("%d %d", &iN, &iB);

	for (iI = 0; iI < iN; iI++)
		scanf("%d", &iData[iI]);

	sort(iData, iData + iN);

	iI = 0;
	iJ = iN - 1;

	while (iI <= iJ) {

		if ((iData[iI] + iData[iJ]) <= iB)
			iI++;

		iJ--;
		iAnswer++;

	}

	printf("%d\n", iAnswer);

	return 0;

}