#include <cstdio>

void soma(float a, int b,int c){
    float resultado = a+b-c;
    printf("A soma e: %.2f\n",resultado);

}

int main(){

    float a;
    int b,c;
    a = 320.9;
    b = 23;
    c = 13;
    soma(a,b,c);

    return 0;
}