#include <cstdio>
#include <cstdlib>

float media(int n, float *vnotas);

int main(void){

    float vnotas[10];
    float mediaNotas;
    int i;

    for(i = 0; i < 10; i++){
        printf("Digite os valores das notas: ");
        scanf("%f",&vnotas[i]);
    }

    mediaNotas = media(10,vnotas);

    printf("\nMedia = %.1f \n",mediaNotas);

    getchar();
    return 0;
}

float media(int n, float *vnotas){
    int i;
    float m = 0, soma = 0;

    for(i = 0; i < n; i++){
        soma = soma + vnotas[i];
    }

    m = soma / n;

    return m;
}