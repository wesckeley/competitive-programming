#include <cstdio>
#include <set>
#include <vector>

using namespace std;

bool checkSum(set< int >& iB, int iNumber){

  set< int >::iterator iBegin, iEnd;

  if(iB.empty() == true)
    return false;

  iBegin = iB.begin();

  do {

    iEnd = iB.lower_bound(iNumber - *iBegin);

    if((iEnd != iB.end()) && ((*iBegin + *iEnd) == iNumber))
      return true;

    iBegin++;

  } while( iBegin != iB.end());

  return false;

}

int main(void){

  int iN, iM;
  set< int > iA, iB;
  int iNumber, iI;

  scanf("%d %d", &iN, &iM);

  for(iI = 0; iI < iN; iI++){
    scanf("%d", &iNumber);
    iA.insert(iNumber);
  }

  for(iI = 0; iI < iM; iI++){
    scanf("%d", &iNumber);
    if(iA.find(iNumber) != iA.end())
      iB.insert(iNumber);
    else {
      if( checkSum(iB, iNumber) == true)
        iB.insert(iNumber);
      else {
        printf("%d\n", iNumber);
        return 0;
      }
    }
  }

  printf("sim\n");

  return 0;
}
