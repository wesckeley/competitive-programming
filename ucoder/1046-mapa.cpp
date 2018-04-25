#include <bitset>
#include <cstdio>
#include <deque>
#include <set>
#include <utility>
#include <vector>

#define MAX 100000

using namespace std;

long long int connectedCount(vector< vector< int > >& iGraph, bitset< MAX >& bVisited, int iSource){

  deque< int > q;
  vector< int >::iterator it;
  long long iAnswer = 0;

  q.push_back(iSource);
  bVisited[iSource] = true;

  while(q.empty() == false){

    iSource = q.front();
    q.pop_front();

    iAnswer++;

    for(it = iGraph[iSource].begin(); it != iGraph[iSource].end(); it++){
      if(bVisited[*it] == false){
        q.push_back(*it);
        bVisited[*it] = true;
      }
    }
  }

  return iAnswer;

}

int main(void){

  vector< vector< int > > iGraph;
  int iN;
  int iI, iFrom, iTo, iC;
  bitset< MAX > bVisited;
  vector< long long int > iCount;
  int iJ;
  long long int iAnswer;

  scanf("%d", &iN);
  iGraph.resize(iN);

  for(iI = 0; iI < iN - 1; iI++){

    scanf("%d %d %d", &iFrom, &iTo, &iC);

    if( iC != 1) {
      iFrom--;
      iTo--;
      iGraph[iFrom].push_back(iTo);
      iGraph[iTo].push_back(iFrom);
    }

  }

  bVisited.reset();
  for(iI = 0; iI < iN; iI++)
    if(bVisited[iI] == false)
      iCount.push_back(connectedCount(iGraph, bVisited, iI));

  iAnswer = 0;
  for(iI = 0; iI < iCount.size(); iI++)
    for(iJ = iI + 1; iJ < iCount.size(); iJ++)
      iAnswer += (iCount[iI] * iCount[iJ]);

  printf("%lld\n", iAnswer);

  return 0;

}
