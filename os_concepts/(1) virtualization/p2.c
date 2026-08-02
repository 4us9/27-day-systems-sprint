#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/wait.h> 

/*With wait, it is guaranteed to wait until child
process is completed. Then, the parent finishes its job.

It is always the order of 
1. child
2. parent

In p1.c, the order is NOT deterministic.
*/
int main(int argc, char *argv[]) {

    printf("hello (pid: %d)\n", (int) getpid());
    int rc = fork(); //create a new child process

    if (rc < 0) {

        fprintf(stderr, "fork failed\n");
        exit(1);
    }

    else if (rc == 0) {

        printf("child (pid: %d)\n", (int) getpid());
    }

    else {
        //parent process calls wait to finish child before running its own
        int rc_wait = wait(NULL); 
        printf("parent of %d (rc_wait: %d) (pid: %d)\n", rc, rc_wait, (int) getpid());
    }

    return 0;
}
