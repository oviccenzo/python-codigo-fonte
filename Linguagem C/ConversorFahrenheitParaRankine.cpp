//
// Created by Robert L Resende on 01/12/24.
//
#include "cstdio"

int main(){

    float centigrado,fahrenheit;

    printf("Digite a conversao centigrado para fahrenheit: \n");
    scanf("%f",&centigrado);

    printf("celsius \t fahrenheit\n");


    for(centigrado = -30; centigrado <= 30; centigrado++) {
        fahrenheit = (9 * centigrado / 5) + 32;
        printf("%.2f  \t %.2f\n",centigrado,fahrenheit);

//        printf("A conversao de centigrado para fahrenheit e: %.2f\n",fahrenheit,centigrado);

    }
}