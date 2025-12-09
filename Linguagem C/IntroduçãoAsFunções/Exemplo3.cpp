#include <cstdio>
int ElevarAoQuadrado(int a);  /* Protótipo de função */
int main(){

    int num;
    printf("Entre com um numero: ");
    scanf("%d",&num);
    num = ElevarAoQuadrado(num); /* Utilização da função */
    printf("\n\nO seu quadrado vale: %d\n",num);
    return 0;
}
int ElevarAoQuadrado(int a){ /* Descrição da função */
    return(a*a);
}