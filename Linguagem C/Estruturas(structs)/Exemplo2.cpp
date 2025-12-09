//
// Created by Robert L Resende on 14/12/24.
//
#include "cstdio"
#include "cstring"

struct pessoa{

    int idade;
    char trabalha[4];
    char estuda[4];
};

int main(){

    struct pessoa A,M;
    A.idade = 18;

    strcpy(A.trabalha,"sim");
    //A.trabalha[3] = 'sim';
    strcpy(A.estuda,"nao");
    //A.estuda[3] = 'nao';
    M = A; //Variavel M recebe todos os campos de A
    printf("Pessoa A: %d %s %s \n",A.idade,A.trabalha,A.estuda);
    printf("Pessoa M: %d %s %s \n",M.idade,M.trabalha,M.estuda);
    getchar();
}