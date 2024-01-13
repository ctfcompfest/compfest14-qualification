#include<stdio.h>
#include<stdlib.h>
#include<string.h>

void sendMail(char *mail){
	puts("\nThis app can only send a mail three days to the past maximum.");
	puts("How many days into the past do you want to send this mail?");
	printf("> ");

	int inp;
	scanf("%d%*c", &inp);

	if (inp > 3){
		puts("What did i just say :/");
		return;
	}
	if (inp < 0){
		puts("You can't send a mail into the future");
		return;
	}

	puts("Enter your mail content");
	printf("> ");
	read(0, mail+((3-inp)*8), 8);
}

void readMail(char *mail){
	puts("\nThis app can only read a mail three days to the past maximum.");
	puts("which mail do you want to read? (input how many days into the past)");
	printf("> ");

	int inp;
	scanf("%d%*c", &inp);

	if (inp > 3){
		puts("Can't read that mail anymore :(");
		return;
	}
	if (inp < 0){
		puts("Are you trying to read a mail from the future?");
		return;
	}

	printf(mail+((3-inp)*8));
}

void win(){
	system("cat flag.txt");
}