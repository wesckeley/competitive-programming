#include <stdio.h>

#define MAX 1000

int main(void){

  int iTestsCount;
  int iN, iM, iI, iJ, iK, iQ;
  int iSum[MAX], iSumTotal = 0;
  double lfAnswer;
  int iAnswer;

  scanf("%d",&iTestsCount);

  for(; iTestsCount > 0; iTestsCount--){

    scanf("%d %d", &iN, &iM);

    for(iI = 0; iI < iM; iI++){
      iSum[iI] = 0;
      iSumTotal = 0;
    }


    for(iI = 0; iI < iN; iI++){
      for(iJ = 0; iJ < iM; iJ++){
        scanf("%d", &iK);
        iSum[iJ] += iK;
        iSumTotal += iK;
      }
    }

    scanf("%d", &iQ);
    iQ--;

    lfAnswer = (double)iSum[iQ] / (double)iSumTotal;
    lfAnswer *= 1000;
    iAnswer = (int) lfAnswer;
    iAnswer -= (iAnswer % 10);
    lfAnswer = ((double)iAnswer) / 1000;

    printf("%.2lf\n",lfAnswer);

  }

  return 0;

}
