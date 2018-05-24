#include <bitset>
#include <deque>
#include <iostream>
#include <string>
#include <utility>

#define MAX 1000

using namespace std;

const int dx[4] = {-1, 0, 1, 0};
const int dy[4] = {0, -1, 0, 1};

int main(void) {

  int iN;
  int iI, iJ;
  string strData[MAX];
  deque< pair< int, int > > q;
  bitset< MAX > bOnQueue[MAX];
  int x, y, to_x, to_y;

  ios_base::sync_with_stdio(false);
  cin.tie(NULL);

  cin >> iN;

  for(iI = 0; iI < iN; iI++) {
    cin >> strData[iI];
    bOnQueue[iI].reset();
  }

  for(iI = 0; iI < iN; iI++) {
    for(iJ = 0; iJ < iN; iJ++) {
      if(strData[iI][iJ] == '*')
        strData[iI][iJ] = '9';
      else {
        q.push_back(pair< int, int >(iI, iJ));
        bOnQueue[iI][iJ] = true;
      }
    }
  }

  while(q.empty() == false) {
    x = q.front().first;
    y = q.front().second;
    q.pop_front();
    bOnQueue[x][y] = false;

    for(iI = 0; iI < 4; iI++) {
      to_x = x + dx[iI];
      to_y = y + dy[iI];

      if((0 <= to_x) && (0 <= to_y) && (to_x < iN) && (to_y < iN)){
        if(strData[to_x][to_y] > (strData[x][y] + 1)){
          strData[to_x][to_y] = strData[x][y] + 1;
          if(bOnQueue[to_x][to_y] == false){
            q.push_back(pair< int, int >(to_x, to_y));
            bOnQueue[to_x][to_y] = true;
          }
        }
      }
    }
  }

  for(iI = 0; iI < iN; iI++)
    cout << strData[iI] << endl;

  return 0;
}
