/*
exec() sys call

Useful to run a program different from the calling program

fork() is only useful to keep running copies of the same
program. But for different programs, exec() helps here.

*/

#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <sys/wait.h>

int main(int argc, char *argv[]) {
    printf("hello (pid: %d)\n", (int) getpid());
    int rc = fork();

    if (rc < 0) {

        fprintf(stderr, "fork failed\n");
        exit(1);
    }
    else if (rc == 0) {
        printf("child (pid: %d) \n", (int) getpid());
        char *myargs[3]; //The 4th elem of the char array is for the null terminator

        myargs[0] = strdup("wc"); //program: "wc"
        myargs[1] = strdup("p3.c"); //arg: input file
        myargs[2] = NULL; //runs word count

        execvp(myargs[0], myargs); //runs the word count (wc) program
        printf("this shouldn't print out");
    }
    else {
        int rc_wait=wait(NULL);
        printf("parent of %d (rc_wait:%d) (pid:%d)\n", rc, rc_wait, (int) getpid());
    }
    return 0; 
}