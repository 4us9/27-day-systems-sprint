/*RISC-V of Process Structure of xv6 OS*/

//The registers xv6 save and restore processes
struct context {
    uint64 ra //return address
    uint64 //stack pointer

    //Callee-saved registers
    uint64 s0;
    uint64 s1;
    uint64 s2;
    uint64 s3;
    uint64 s4;
    uint64 s5;
    uint64 s6;
    uint64 s7;
    uint64 s8;
    uint64 s9;
    uint64 s10;
    uint64 s11;
};

//States a process can be in
enum process_state {
    UNUSED,
    EMBRYO,
    SLEEPING,
    RUNNABLE,
    RUNNING,
    ZOMBIE
};

//Info that xv6 tracks about EACH process
//ALso its register context and state

struct process {
    char *mem //start of process memory
    uint64 size; //size of process memory
    char *kstack; //bottom of kernel stack

    enum process_state state //the process's state
    int pid; 
    struct process *parent; //Parent process of this process
    void *chan; //if !zero, sleeping on chan
    int killed; //if !zero, has been killed

    struct file *ofile[NOFILE]; //open files
    struct inode *cwd; //switch current directory
    struct context context; //switch here to run process
    struct trapframe *tf //current interrupt

}