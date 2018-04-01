#include <cstdio>

int main(void) {

	int iA, iB, iC, iD;

	scanf("%d %d %d %d", &iA, &iB, &iC, &iD);

	((iA == iC) || (iB == iD)) ? printf("V\n") : printf("F\n");

	return 0;

}