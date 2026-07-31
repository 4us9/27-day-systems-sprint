#include <stdio.h>
#include <stdlib.h>
#include "common.h"
#include "common_threads.h"

/*Concurrency: Working on many things at once in the same program*/

//Modern problems of concurrency: multi-threaded programs + OS.
volatile int counter = 0;
int loops;

void *worker(void *arg) {
    int i;
    for (i=0; i<loops; i++) {

        counter++;
    }

    return NULL;


}

int main(int argc, char *argv[]) {
    if (argc != 2) {

        fprintf(stderr, "usage: threads<value> \n");
        exit(1);
    }

    loops = atoi(argv[1]); //1. text receives from command line and store in loops
    pthread_t p1, p2; //`pthread_t` type. Creates two threads

    printf("Initial value: %d\n", counter);

    //Program creates two threads
    //Each thread increments `counter` of `loops` times
    Pthread_create(&p1, NULL, worker, NULL); //routine called worker that increments `loops`
    Pthread_create(&p2, NULL, worker, NULL);


    //Wait for both to finish
    Pthread_join(p1, NULL);
    Pthread_join(p2, NULL);


    //Final output
    printf("Final value: %d\n", counter);
    return 0;

}

//this program does not run atomically (load value of ctr from MEM to reg, increment, store into MEM)
//Therefore a problem with concurrency. Does not give expected value at all times. 