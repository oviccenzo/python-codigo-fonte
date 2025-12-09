#include <cstdio>
int main(){

    int cont = 0;

    printf("Digite uma frase: \n");
    while(getchar()!='\r')  //caractere <enter>
        cont ++;
    printf("\n O numero de caracteres eh %d \n",cont);

    return 0;
}