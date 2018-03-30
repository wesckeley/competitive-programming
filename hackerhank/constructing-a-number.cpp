#include <cstdio>

int getSum(int iNumber){

    int iAnswer = 0;

    while(iNumber > 0){
        iAnswer += iNumber % 10;
        iNumber /= 10;
    }

    return iAnswer;

}

int main(void){

    int iT, iN, iNumber, iDigitSum;

    scanf("%d", &iT);

    for( ; iT > 0; iT--){

        scanf("%d", &iN);
        iDigitSum = 0;

        for( ; iN > 0; iN--){
            scanf("%d", &iNumber);
            iDigitSum += getSum(iNumber);
        }

        ((iDigitSum % 3) == 0) ? printf("Yes\n") : printf("No\n");
        
    }

    return 0;

}