#include <cstdio>
int EPar(int a){
    if(a%2)         /* Verifica se a divisível por dois */
        return 0;  /* Retorna 0 se não for divisível */
    else
        return 1; /* Retorna 1 se for divisível */
}

int main(){

    int num;
    printf("Entre com numero: ");
    scanf("%d",&num);
    if(EPar(num))
        printf("\n\nO numero e par.\n");
    else
        printf("\n\nO numero e impar.\n");
    return 0;
}
