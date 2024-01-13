#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include "libtcmail.h"

void init() {
    setvbuf(stdout, NULL, _IONBF, 0);
}

int menu() {
    puts("\nMenu:");
    puts("1. Send mail");
    puts("2. Read mail");
    puts("3. Exit");
    printf("> ");
    
    int choice;
	scanf("%d", &choice);
	return choice;
}


int main(){
	char mail[32];

	init();
	memset(mail, 0, 32);
	while(1){
		int choice = menu();
		if (choice == 1){
			sendMail(mail);
		}
		if (choice == 2){
			readMail(mail);
		}
		if (choice == 3){
			puts("Bye.");
			exit(0);
		}
	}
}