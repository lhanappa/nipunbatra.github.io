#include <stdio.h>

#include "mythreads.h"

int balance = 0;
int lock = 0;

void* worker(void* arg) {
    while(lock);
    lock=1;
    balance++; // unprotected access
    lock = 0; 
    return NULL;
}

int main(int argc, char *argv[]) {
    pthread_t p;
    Pthread_create(&p, NULL, worker, NULL);
    while(lock);
    lock = 1;
    balance++; // unprotected access
    lock = 0;
    Pthread_join(p, NULL);
    return 0;
}
