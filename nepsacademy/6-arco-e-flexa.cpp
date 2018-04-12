#include <algorithm>
#include <cstdio>
#include <utility>

#define MAX 100000

using namespace std;

void ftUpdate(int* ft, int iI, int iN) {

	while (iI <= iN) {
		ft[iI]++;
		iI += iI & (-iI);
	}

}

long long int ftQuery(int *ft, int iI) {

	long long int iAnswer = 0;

	while (iI > 0) {
		iAnswer += ft[iI];
		iI -= iI & (-iI);
	}

	return iAnswer;

}

int main(void){

    int iN, iI, iJ;
    pair< long long int, int > iDistances[MAX];
    int iData[MAX];
    long long int iX, iY;
    long long int iAnswer = 0;
    int ft[(MAX + 1)];

    scanf("%d",&iN);

    for(iI = 0; iI < iN; iI++){
        scanf("%lld %lld",&iX,&iY);
        iDistances[iI].first = (iX * iX) + (iY * iY);
        iDistances[iI].second = iI;
    }

    sort(iDistances,iDistances + iN);

    iJ = 1;
    iData[iDistances[0].second] = iJ;

    for(iI = 1; iI < iN; iI++){
        if(iDistances[iI].first != iDistances[(iI - 1)].first)
            iJ++;
        iData[iDistances[iI].second] = iJ;
    }

    for(iI = 0; iI <= iN; iI++)
        ft[iI] = 0;

    for(iI = 0; iI < iN; iI++){

        iAnswer += ftQuery(ft,iData[iI]);
        ftUpdate(ft,iData[iI],iN);

    }

    printf("%lld\n",iAnswer);

    return 0;
}