#include <stdio.h>	
#include <pthread.h>
#include <assert.h>

int counter;
pthread_mutex_t lock;

void *counter_thread(void *arg){

	int i = 0;

	printf("Thread %s begins\n",(char *)arg);

	while(i < 1000000){
		pthread_mutex_lock(&lock);
		counter = counter + 1;
		pthread_mutex_unlock(&lock);
		//printf("%s : %d\n",(char *)arg,counter);
		i = i + 1;
	}
	return NULL;
}

int main(){
	pthread_t t1,t2;
	int rc;
	
	printf("Main:begin\n");

	if(pthread_mutex_init(&lock,NULL) != 0){
		printf("Mutex initialization failed\n");
		return 1;
	}
	
	rc = pthread_create(&t1,NULL,counter_thread,"A");
	assert(rc==0);	

	rc = pthread_create(&t2,NULL,counter_thread,"B");
	assert(rc==0);

	pthread_join(t1,NULL);
	pthread_join(t2,NULL);

	pthread_mutex_destroy(&lock);
	printf("Main:End %d",counter);
	return 1;		
}
