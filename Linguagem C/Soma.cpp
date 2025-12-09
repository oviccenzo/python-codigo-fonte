#include <cstdio>

void soma(float a, int b){
    float resultado;

    resultado = a + b;

    printf("A soma de %6.3f com %d e %6.3f\n",a,b,resultado);

}

int main(){

    int a;
    float b;

    a = 10;
    b = 12.3;
    soma(b,a);

    return 0;
}