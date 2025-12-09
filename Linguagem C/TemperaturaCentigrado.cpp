#include <cstdio>

int main(){

    float faharenheit,centigrado;

    printf("Digite a temperatura fahrenheit: ");
    scanf("%f",&faharenheit);

    printf("celsius \t fahrenheit\n");

    for(centigrado = -30; centigrado <= 30;centigrado++){
        faharenheit = (9 * centigrado / 5) + 32;
        printf("%.2f  \t %.2f\n",centigrado,faharenheit);
    }
}



