#include <bitset>
#include <vector>
#include <utility>

#define MAX 10000000

using namespace std;

bitset<( MAX + 1)> bIsPrime;
vector< int > iPrimes;

void getDivisors(long long int& iNumber, vector< pair< long long int, int > >& iList){

  int iN = iPrimes.size();
  int iI = 0;

  iList.clear();

  while((iNumber > 1) && (iI < iN)){

    if((iNumber % iPrimes[iI]) == 0){
      if(iList.size() == 0)
        iList.push_back(pair<long long int, int>(iPrimes[iI], 1));
      else {
        if(iList[(iList.size() - 1)].first == iPrimes[iI])
          iList[(iList.size() - 1)].second++;
        else
          iList.push_back(pair<long long int, int>(iPrimes[iI], 1));
      }
      iNumber /= iPrimes[iI];
    }
    else
      iI++;
  }

}

int getDivisorsBruteForte(long long int iNumber){

  int iI;
  int iAnswer = 0;

  for(iI = MAX; (iI * iI) <= iNumber; iI++)
    if(((iNumber) % iI) == 0)
      iAnswer++;

  return iAnswer;

}

int main(void){

  int iI, iJ;
  vector< pair< long long int, int > > iDivisors;
  long long int iNumber;
  int iAnswer = 0;

  bIsPrime.set();
  for(iI = 2; (iI * iI) <= MAX; iI++)
    if(bIsPrime[iI] == true)
      for(iJ = (iI * iI); iJ <= MAX; iJ += iI)
        bIsPrime[iJ] = false;

  for(iI = 2; iI <= MAX; iI++)
    if(bIsPrime[iI] == true)
      iPrimes.push_back(iI);

  while(scanf("%lld",&iNumber) != EOF){

    getDivisors(iNumber,iDivisors);

    iAnswer = 1;
    for(iI = 0; iI < iDivisors.size(); iI++)
      iAnswer *= (iDivisors[iI].second + 1);

    iAnswer += getDivisorsBruteForte(iNumber);

    printf("%d\n", iAnswer);

  }

  return 0;
}
