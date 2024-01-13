#include<stdio.h>
#include<stdlib.h>
#include<string.h>

void win(){
	system("cat flag.txt");
}

int main(){
	setvbuf(stdout, NULL, _IONBF, 0);

	char message[72];

	puts("Tell me about yourself");
	gets(message);

	if (strlen(message)>64){
		puts("You talk too much");
		exit(0);
	}

	puts("Who are you");

	return 0;
}