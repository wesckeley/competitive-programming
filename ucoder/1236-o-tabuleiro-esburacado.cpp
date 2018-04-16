#include <bitset>
#include <cstdio>

using namespace std;

const int iMovX[8] = { 1, 2, 2, 1, -1, -2, -2, -1};
const int iMovY[8] = { 2, 1, -1, -2, -2, -1, 1, 2};

int main( void){
    
    bitset<8> bMap[8];
    int iN, iX, iY;
    int iMov;
    
    for( auto iI = 0; iI < 8; iI++)
        bMap[iI].reset();
    
    bMap[1][3] = true;
    bMap[2][3] = true;
    bMap[2][5] = true;
    bMap[5][4] = true;
    
    scanf( "%d\n", &iN);
    
    iX = 4;
    iY = 3;
    
    for( auto iI = 1; iI <= iN; iI++){
        
        scanf( "%d", &iMov);
        iMov--;
        
        iX += iMovX[iMov];
        iY += iMovY[iMov];
        
        if( bMap[iX][iY] == true){
            
            printf( "%d\n", iI);
            return 0;
            
        }
    }
    
    printf( "%d\n", iN);
    
}