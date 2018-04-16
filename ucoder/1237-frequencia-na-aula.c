#include <stdio.h>

#ifdef WIN32
#define getchar_unlocked _getchar_nolock
#endif

#define MAX 1000000

char chFlag[(MAX + 1)];

void fastscan(int *x){

    register int c = 0;
    
    *x = 0;

    for(;c < '0' || c > '9'; c = getchar_unlocked());

    for(;c >= '0' && c <= '9'; c = getchar_unlocked()){
        *x = ((*x) << 1) + ((*x) << 3) + (c - '0');
    } 

}

int main(void){

    int iN, iNumber, iAnswer = 0;

    fastscan(&iN);

    for(;iN > 0;iN--){

        fastscan(&iNumber);
        
        if(chFlag[iNumber] == 0)
            iAnswer++;
        
        chFlag[iNumber] = 1;
    }

    printf("%d\n",iAnswer);

    return 0;

}