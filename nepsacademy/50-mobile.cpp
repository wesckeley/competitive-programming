#include <cstdio>

int main(void) {

	int iA, iB, iC, iD;
	bool bAnswer;

	scanf("%d %d %d %d", &iA, &iB, &iC, &iD);

	bAnswer = (iA == (iB + iC + iD));
	bAnswer &= (iD == (iB + iC));
	bAnswer &= (iB == iC);

	(bAnswer == true) ? printf("S\n") : printf("N\n");

	return 0;

}