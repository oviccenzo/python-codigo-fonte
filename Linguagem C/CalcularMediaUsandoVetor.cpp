#include <cstdio>

int main(){


    float nota[3];
    float media,m,s;

    //nota 1
    printf("Digite a primeiro nota: ");
    scanf("%f",&m);
    printf("Digite a segunda nota: ");
    scanf("%f",&s);
    nota[0] = m + s;

    //nota 2
    printf("Digite a terceira nota: ");
    scanf("%f",&m);
    printf("Digite a quarta nota: ");
    scanf("%f",&s);
    nota[1] = m + s;

    //nota 3
    printf("Digite a quinta nota: ");
    scanf("%f",&m);
    printf("Digite a sexta nota: ");
    scanf("%f",&s);
    nota[2] = m + s;

    media = (nota[0] + nota[1] + nota[2])/10;

    printf("A media das tres nota e: %.2f\n",media);
}