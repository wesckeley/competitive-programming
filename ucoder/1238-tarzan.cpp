#include <bitset>
#include <cstdio>
#include <deque>
#include <utility>
#include <vector>

#define MAX 1000

#ifdef _WIN32
#define getchar_unlocked _getchar_nolock
#endif

using namespace std;

void fastscan(int &x){

    int c = 0;
    
    x = 0;

    for(;c < '0' || c > '9'; c = getchar_unlocked());

    for(;c >= '0' && c <= '9'; c = getchar_unlocked()){
        x = (x << 1) + (x << 3) + (c - '0');
    } 

}

bool checkDistance(int x, int y, int _x, int _y, int d){

    x -= _x;
    y -= _y;
    x *= x;
    y *= y;
    d *= d;
    return (x + y) <= d;

}

int bfs(vector< vector< int > > iGraph){

    bitset< MAX > bVisited;
    deque< int > q;
    int u, iAnswer = 0;
    vector< int >::iterator it;

    bVisited.reset();
    bVisited[0] = true;
    q.push_back(0);

    while(q.empty() == false){

        u = q.front();
        q.pop_front();

        iAnswer++;

        for(it = iGraph[u].begin(); it != iGraph[u].end(); it++){
            if(bVisited[*it] == false){
                q.push_back(*it);
                bVisited[*it] = true;
            }
        }

    }

    return iAnswer;

}

int main(void){

    int iN, iD, iI, iJ;
    vector< vector< int > > iGraph;
    vector< pair< int, int > > iPoint;

    fastscan(iN);
    fastscan(iD);

    iGraph.resize(iN);
    iPoint.resize(iN);

    for(iI = 0; iI < iN; iI++){
        fastscan(iPoint[iI].first);
        fastscan(iPoint[iI].second);
    }

    for(iI = 0; iI < iN; iI++){
        for(iJ = iI + 1; iJ < iN; iJ++){
            if(checkDistance(iPoint[iI].first,iPoint[iI].second,iPoint[iJ].first,iPoint[iJ].second,iD) == true){
                iGraph[iI].push_back(iJ);
                iGraph[iJ].push_back(iI);
            }
        }
    }

    (iN == bfs(iGraph)) ? printf("S\n") : printf("N\n");

    return 0;

}