#include <cstdio>
#include <cstring>
int main(){
    char str1[10],str2[10];
    scanf("%s",str1,str2);
    if(strcmp(str1,str2) != 0)
        printf("\n\nAs duas strings são diferentes.");
    else
        printf("\n\nAs duas strings são iguais");
    return 0;
}