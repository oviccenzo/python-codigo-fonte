#include <cstdio>
int ElevarAoQuadrado(int a,int e)
{
    return(a*a +  e);
}

int main()
{
    int num;
    printf("Entre com um numero: ");
    scanf("%d",&num);
    num = ElevarAoQuadrado(num,num);
    printf("\n\nO seu quadrado vale: %d\n",num);
    return 0;
}