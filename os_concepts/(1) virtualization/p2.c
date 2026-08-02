#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/wait.h> 

int main(int argc, char *argv[]) {

    printf("hello (pid: %d)\n", (int) getpid());
    int rc = fork(); //create a new child process

    if (rc < 0) {

        
    }
}