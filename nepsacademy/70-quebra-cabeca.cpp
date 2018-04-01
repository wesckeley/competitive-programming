#include <cstdio>

#define MAX 200000
#define ANSWER_MAX 100000

typedef struct {

	char chChar;
	int iRight;

} node;

int main(void) {

	int iN, iI, iStartNode;
	node iGraph[(MAX + 1)];
	int iLeftCount[(MAX + 1)], iRightCount[(MAX + 1)];
	int iLeft, iRight;
	char chChar;
	char chAnswer[(ANSWER_MAX + 1)];

	for (iI = 0; iI <= MAX; iI++) {

		iLeftCount[iI] = 0;
		iRightCount[iI] = 0;
		iGraph[iI].iRight = -1;

	}

	scanf("%d", &iN);

	for (iI = 0; iI < iN; iI++) {

		scanf("%d %c %d", &iLeft, &chChar, &iRight);

		iLeftCount[iLeft]++;
		iRightCount[iRight]++;

		iGraph[iLeft].chChar = chChar;
		iGraph[iLeft].iRight = iRight;

	}

	iStartNode = -1;
	for (iI = 0; ((iI <= MAX) && (iStartNode == -1)); iI++)
		if ((iLeftCount[iI] == 1) && (iRightCount[iI] == 0))
			iStartNode = iI;

	iI = 0;

	do {

		chAnswer[iI] = iGraph[iStartNode].chChar;
		iStartNode = iGraph[iStartNode].iRight;
		iI++;

	} while (iGraph[iStartNode].iRight != -1);

	chAnswer[iI] = '\0';

	printf("%s\n", chAnswer);

	return 0;
}