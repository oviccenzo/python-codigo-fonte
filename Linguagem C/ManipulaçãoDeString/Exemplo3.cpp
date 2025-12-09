#include <cstdio>
#include <cstring>
int main()
{
    char str1[50],str2[50];
    scanf("%s",str1);
    strcpy(str2,"Voce digitou a string: ");
    strcat(str2,str1);
    printf("\n\n%s",str2);
    return 0;
}