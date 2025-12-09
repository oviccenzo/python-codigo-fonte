#include <cstdio>
int main()
{
    float z;
    int x,y;
    x = 8;
    y = 3;

    z = (int)(x/y); /* z recebe 2.0 */

    printf("O resultado de z é: %f",z);

    return 0;
}