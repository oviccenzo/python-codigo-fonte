#include <cstdio>

void nota(float nota1,float nota2){

    float resultado;

    resultado = (nota1 + nota2) / 2.0;

    printf("A media das duas nota e: %.2f\n",resultado);
}


int main(){

    float nota1,nota2;

    printf("Digite a primeira nota: ");
    scanf("%f",&nota1);

    printf("Digite a segunda nota: ");
    scanf("%f",&nota2);

    nota(nota1,nota2);
}