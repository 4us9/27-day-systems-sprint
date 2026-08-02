#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

/*
It is interesting how strange fork() system call is. It creates a child process then resumes from that spot. So effectively,
parent PID and child PID will both go through the two conditionals, printing both messages from the conditions rc == 0 (child) and rc > 0 (parent) checks.

*/
int main(int argc, char *argv[]) {

    printf("hello (pid: %d)\n", (int) getpid());

    int rc = fork();
    if (rc < 0) {

        //fork failed
        fprintf(stderr, "fork failed\n");
        exit(1);

    }
    else if (rc == 0) {

        //child (new process)
        printf("child (pid: %d) \n", (int) getpid());
    }

    else {
        //parent goes down this path (main)
        printf("\nparent of %d (pid: %d)\n", rc, (int) getpid());

    }
    return 0;
}