#include <cstdio>
int main(){

    int cont,num;

    cont = 0;
    printf("Digite uma sequencia de numeros terminada em zero: \n");
    scanf("%d",&num);
    while(num != 0){
     cont ++;
     scanf("%d",&num);
    }
    printf("\nForam digitados %d numeros.\n",cont);
    return 0;
}