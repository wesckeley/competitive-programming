#include <stdbool.h>
#include <stdio.h>

#define MAX 100000

int main(void){

  int iV, iM;
  int iData[MAX];
  bool dp[(MAX + 1)];
  int iI, iJ;

  scanf("%d %d", &iV, &iM);

  for(iI = 0; iI < iM; iI++)
    scanf("%d", &iData[iI]);

  for(iI = 0; iI <= iV; iI++)
    dp[iI] = false;
  dp[0] = true;

  for(iI = 0; (iI < iM) && (dp[iV] == false); iI++)
    for(iJ = iV; iJ >= iData[iI]; iJ--)
      dp[iJ] |= dp[iJ - iData[iI]];

  (dp[iV] == true) ? printf("S\n") : printf("N\n");

  return 0;

}
