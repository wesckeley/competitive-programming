#include <bitset>
#include <deque>
#include <iostream>
#include <utility>

#define MAX 101
#define INF 0x1FFFFFFF

using namespace std;

int iMap[MAX][MAX];

const int dx[4] = {-1,0,1,0};
const int dy[4] = {0,-1,0,1};

int dijkstra(int iN) {

  int iCost[MAX][MAX];
  bitset< MAX > bOnQueue[MAX];
  int iI, iJ;
  deque< pair< int, int > > q;
  int iX, iY;

  for(iI = 0; iI < iN; iI++) {
    bOnQueue[iI].reset();
    for(iJ = 0; iJ < iN; iJ++)
      iCost[iI][iJ] = INF;
  }

  iCost[0][0] = 0;
  bOnQueue[0][0] = true;
  q.push_back(pair<int ,int >(0, 0));

  while(q.empty() == false) {

    iX = q.front().first;
    iY = q.front().second;

    bOnQueue[iX][iY] = false;
    q.pop_front();

    iJ = iCost[iX][iY];

    for(iI = 0; iI < 4; iI++) {

      iX += dx[iI];
      iY += dy[iI];

      if((0 <= iX) && (0 <= iY) && (iX < iN) && (iY < iN)) {
        if((iJ + iMap[iX][iY]) < iCost[iX][iY]) {
          iCost[iX][iY] = iJ + iMap[iX][iY];
          if(bOnQueue[iX][iY] == false) {
            bOnQueue[iX][iY] = true;
            q.push_back(pair<int, int>(iX, iY));
          }
        }
      }

      iY -= dy[iI];
      iX -= dx[iI];

    }

  }

  return iCost[(iN - 1)][(iN - 1)];

}

int main(void){

  int iN;
  int iI, iJ;

  ios_base::sync_with_stdio(false);
  cin.tie(NULL);

  cin >> iN;

  for(iI = 0; iI < iN; iI++)
    for(iJ = 0; iJ < iN; iJ++)
      cin >> iMap[iI][iJ];

  cout << dijkstra(iN) << endl;

  return 0;
}
