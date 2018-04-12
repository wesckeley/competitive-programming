#include <cstdio>
#include <deque>
#include <utility>

#define MAX 1000
#define INF 100000

using namespace std;

char chMap[MAX][( MAX + 1)];
int iN, iM;

int iMovN[4] = { -1, 0, 1, 0};
int iMovM[4] = { 0, -1, 0, 1};

int getDistance( int iI, int iJ){
    
    deque< pair< pair< int, int >, int > > q;
    int iK, iD;
    
    q.push_back( pair< pair< int, int >, int >( pair< int, int >( iI, iJ), 0));
    
    while( q.empty() == false){
        
        iI = q.front().first.first;
        iJ = q.front().first.second;
        iD = q.front().second;
        q.pop_front();
        
        for( iK = 0; iK < 4; iK++){
            
            iI += iMovN[iK];
            iJ += iMovM[iK];
            
            if(( 0 <= iI) && ( 0 <= iJ) && ( iI < iN) && ( iJ < iM)){
                
                if( chMap[iI][iJ] == '.'){
                    
                    chMap[iI][iJ] = 'x';
                    q.push_back( pair< pair< int, int >, int >( pair< int, int >( iI, iJ), iD + 1));                    
                    
                }
                else {
                    
                    if( chMap[iI][iJ] == 'T')
                        return iD + 1;
                    
                    
                }
            }
            
            
            iJ -= iMovM[iK];
            iI -= iMovN[iK];
            
            
        }
    }
    
    return INF;
    
}

int main( void){
    
    int iI, iJ, iC;
    
    scanf( "%d %d\n", &iN, &iM);
    
    for( iI = 0; iI < iN; iI++)
        scanf( "%s\n", chMap[iI]);
    
    
    scanf( "%d\n", &iC);
    iC *= 4;
    
    for( iI = 0; iI < iN; iI++)
        for( iJ = 0; iJ < iM; iJ++)
            if( chMap[iI][iJ] == 'S')                
                iC -= getDistance( iI, iJ);

        
    if( iC >= 0)
        printf( "SIM\n");
    else
        printf( "NAO\n");
    
    return 0;
    
}