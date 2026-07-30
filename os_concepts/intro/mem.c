#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>
#include "common.h"

//Program that accesses memory 

int main(int argc, char *argv[]) {
    int *p = malloc(sizeof(int)); 
    assert(p != NULL);

    printf("(%d) address pointed to by p: %p\n", getpid(), p);

    *p = 0;

    while(1) {
        Spin(1);
        *p = *p+1;
        printf("(%d) p: %d\n", getpid(), *p); //get pid followed by accessing the value of p

    }
    return 0;

}