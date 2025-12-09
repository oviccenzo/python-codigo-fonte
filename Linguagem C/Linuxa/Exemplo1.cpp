//
// Created by Robert L Resende on 18/05/25.
//

#include <unistd.h>
//#include <sys/types.h>
#include <cstdio>

//int main(){
//    pid_t pid = getpid();
//    printf("PID atual %d\n", pid);
//
//    return 0;
//
//}

int main(){
    pid_t pid = fork();

    if(pid == 0){
        printf("Processo filho\n");
    } else if(pid > 0){
        printf("Processo pai\n");
    } else{
        perror("Fork falhou");
    }
}