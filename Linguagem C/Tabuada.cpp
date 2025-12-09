#include "cstdio"

int main(){

    int numero,i;

    printf("Digite um numero: ");
    scanf("%d",&numero);

    for(i = 0; i < 11;i++){

        printf("%d * %d = %d\n",numero,i,numero*i);
    }
}

