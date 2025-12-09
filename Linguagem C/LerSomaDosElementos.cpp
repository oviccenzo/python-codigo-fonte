#include <cstdio>
#define M 10
int a[M];

void fleitura(){
    int i;
    printf("Digite os %d elementos inteiros: \n",M);
    for(i = 0; i < M; i++){
        scanf("%d", &a[i]);
    }
}

int fsoma(){
    int soma , i;
    soma = 0;
    for(i = 0; i < M; i++){
        soma = soma + a[i];
    }
    return soma;
}

void fimprime(){
    int i;
    printf("\nElementos do vetor: \n");
    for(i = 0; i < M; i++){
        printf("%d\n", a[i]);
    }
}

int main(){

    fleitura();
    printf ("\nA soma dos elementos e  %d \n", fsoma());
    fimprime();
    return 0;
}