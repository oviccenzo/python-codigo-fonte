#include <cstdio>
void esperaEnter(){

    int tecla;
    printf("Pressione Enter\n");
    do{
        tecla = getchar();
        if(tecla != 13){
            printf("Digite Enter\n");
        }
    } while(tecla != 13);
}

int main(){

    esperaEnter();
    //-----------
    esperaEnter();
    //-----------
    esperaEnter();
}