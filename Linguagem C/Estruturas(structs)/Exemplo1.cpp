//
// Created by Robert L Resende on 14/12/24.
//
#include "cstdio"
#include "cstdlib"

struct ponto{
    int  x;
    int y;
};


int main(){

    struct ponto P,M;

    printf("Digite o ponto P: \n");
    scanf("%d  %d",&P.x,&P.y);
    printf("P = (%d %d)\n",P.x,P.y);
    printf("\nDigite o ponto M: \n");
    scanf("%d  %d",&M.x,&M.y);
    printf(" M = (%d %d)\n",M.x,M.y);

    getchar();
    return 0;
}