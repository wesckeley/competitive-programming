#include <stdio.h>

#ifdef WIN32
#define getchar_unlocked _getchar_nolock
#endif

#define MAX 60000

int ft_data[(MAX + 1)];

void ft_update(int iI, int iN){

    for(; iI <= iN; iI += (iI & (-iI)))
        ft_data[iI]++;

}

int ft_query(int iI){

    int iAnswer = 0;

    for(; iI > 0; iI -= (iI & (-iI)))
        iAnswer += ft_data[iI];

    return iAnswer;
        
}

void fastscan(int *x){

    register int c = 0;
    
    *x = 0;

    for(;c < '0' || c > '9'; c = getchar_unlocked());

    for(;c >= '0' && c <= '9'; c = getchar_unlocked()){
        *x = ((*x) << 1) + ((*x) << 3) + (c - '0');
    } 

}

int main(void){

    int iN, iI;
    int iData[MAX];
    int iAnswer = 0;

    fastscan(&iN);
    for(iI = 0; iI < iN; iI++)
        fastscan(&iData[iI]);

    for(iI = iN - 1; iI >= 0; iI--){
        iAnswer += ft_query(iData[iI] - 1);
        ft_update(iData[iI], iN);
    }

    printf("%d\n", iAnswer);

    return 0;
}