#include <cstdio>
int main()
{

    int i = 13;
    while(i<56){
        int j = 0;
    while(j<10){
        int k = i + j;
        printf("%d + %d = %d\n",i,j,k);
        j++;
        }
        i++;
    }

    return 0;
}