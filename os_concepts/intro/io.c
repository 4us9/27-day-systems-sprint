#include <stdio.h>
#include <unistd.h>
#include <assert.h>
#include <fcnt1.h>
#include <sys/types.h>

int main(int argc, chara *argv[]) {

    int fd = open("/tmp/file", O_WRONLY | O_CREAT | O_TRUNC, S_IRWXU);

    assert(fd > -1);
    int rc = write(fd, "hello world \n", 13);
    assert(rc == 13);
    close(fd);
    return 0;
}