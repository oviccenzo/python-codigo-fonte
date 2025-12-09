#include <cstdio>

int main(){

    float vet[6];
    float media,soma = 0;

    printf("Primeiro elemento do vetor: ");
    scanf("%f",&vet[0]);

    printf("Decimo elemento do vetor: ");
    scanf("%f",&vet[1]);

    printf("Terceiro elemento do vetor: ");
    scanf("%f",&vet[2]);

    printf("Quarto elemento do vetor: ");
    scanf("%f",&vet[3]);

    printf("Quinto elemento do vetor: ");
    scanf("%f",&vet[4]);

    printf("Sexto elemento do vetor: ");
    scanf("%f",&vet[5]);

    for(int i = 0; i < 6; i++){
        soma = vet[i];
    }

    media = soma/6;

    printf("A media das 6 nota e: %.2f\n",media);
}