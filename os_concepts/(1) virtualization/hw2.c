/*
Write a program that calls fork(). Before calling fork(), 
have the main process access a variable (e.g., x) and set its value
to something (e.g., 100). What value is the variable in the
child process? What happens to the variable when both the child 
and parent change the value of x? 
*/

#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>

int main(){

    int x = 100; //initial value

    pid_t pid = fork();

    printf("Child & parent initially sees %d \n", x);

    if (pid == 0) {
        x = 42;
        printf("Child changed x to %d\n", x);
    }
    else {
        wait(NULL); //wait for child to finish
        printf("Parent still sees the shared vairable %d\n", x);
    }



    return 0;
}
