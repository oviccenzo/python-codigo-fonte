#include <cstdio>

int main(){

    float notas[5];
    float media,soma = 0;
    printf("Digite as notas de 5 alunos: \n");
    for(int i = 0; i < 5; i++){
        scanf("%f",&notas[i]);
    }
    for(int i = 0; i < 5; i++){
        soma = soma + notas[i];
    }
    media = soma / 5;
    printf("A media das notas e: %.2f\n",media);

    
}