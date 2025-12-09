//O while e muito pratico em situação onde
//não se sabe quantas vezes um comando precisa
//ser executado

#include <cstdio>
int main(){

    char ch;
    ch = '\0';
    while(ch != 'q')
    {
        ch = getchar();
    }
    return 0;
}