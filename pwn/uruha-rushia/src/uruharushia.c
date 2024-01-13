

#include<stdio.h>
#include<stdlib.h>
#include<unistd.h>
#include<time.h>
#include<signal.h>
#include<unistd.h>

struct clip {
    unsigned long long clip_number;
    unsigned long long date_clipped;
    char clip_content[];
};

struct clips {
    struct clip *_clip;
    unsigned long long clip_length;
};

struct clips rushia_clips[16];

void sig_alarm_handler(int signum){
	puts("Connect Timeout");
	exit(1);
}

void init() {
    setvbuf(stdout,  NULL, _IONBF, 0);
    signal(SIGALRM,sig_alarm_handler);
	alarm(60);
}

void menu() {
    puts("1. Clip new Rushia clip");
    puts("2. Delete Rushia clip (why would you do this)");
    puts("3. Edit Rushia clip");
    puts("4. Watch Rushia clip");
    puts("5. Stop clipping Rushia (😭😭😭)");
    printf("> ");
    return;
}

void read_str(char* username, int length)   {
    int len = read(0, username, length);
    if(username[len-1] == '\n')
        username[len-1] = '\0';
    return;
}

unsigned long long read_ulong()    {
    char buf[20];
    read_str(buf, 20);
    return (unsigned long long) strtoll(buf, NULL, 10);
}

void clip_rushia_stream() {
    uint index;
    unsigned long long temp;
    printf("Index: ");
    index = read_ulong();
    if(index < 16) {
        printf("Clip Length: ");
        temp = read_ulong();
        if(temp < 0x500)   {
            puts("おい!何やってんだ？！？！？！");
        }
        else{
            rushia_clips[index]._clip = malloc(sizeof(struct clip) + temp);
            rushia_clips[index]._clip->clip_number = index;
            rushia_clips[index]._clip->date_clipped = (unsigned long)time(NULL);
            rushia_clips[index].clip_length = temp;
            printf("Clip Content: ");
            read(0, rushia_clips[index]._clip->clip_content, temp);
            printf("Done!\n");
        }
    }
    else    {
        puts("おい!何やってんだ？！？！？！");
    }
    return;
}

void delete_clip() {
    uint index;
    printf("Index: ");
    index = read_ulong();
    if(index < 16 && rushia_clips[index]._clip != NULL) {
        free(rushia_clips[index]._clip);
        printf("Done!\n");
    }
    else    {
        puts("おい!何やってんだ？！？！？！");
    }
    return;
}

void edit_clip() {
    uint index;
    printf("Index: ");
    index = read_ulong();
    if(index < 16 && rushia_clips[index]._clip != NULL) {
        printf("Enter new clip data: ");
        read(0, rushia_clips[index]._clip->clip_content, rushia_clips[index].clip_length);
        printf("Done!\n");
    }
    else    {
        puts("おいい!何やってんだ？！？！？！");
    }
    return;
}

void enjoy_rushia() {
    int choice=-1;
    char *username = malloc(0x20);
    
    puts("Awesome, you've decided to start clipping Uruha Rushia");
    printf("Enter your clipper name (max 32 characters): ");
    read_str(username, 32);
    printf("%s, こんるし!\n",  username);

    while(1)    {
        menu();
        choice = read_ulong();
        switch (choice)
        {
        case 1:
            clip_rushia_stream();
            break;
        case 2:
            delete_clip();
            break;
        case 3:
            edit_clip();
            break;
        case 4:
            puts("#TODO: implement watch clip function");
            puts("(this is on purpose)");
            break;
        case 5:
            puts("おつるしああああ!");
            goto end;
        
        default:
            puts("おい!何やってんだ？！？！？！");
            break;
        }
    }
    end:
    return;
}

int main(int argc, char const *argv[])
{
    init();
    enjoy_rushia();
    return 0;
}
