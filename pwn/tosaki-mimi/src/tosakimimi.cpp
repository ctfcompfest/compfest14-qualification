

#include<utility>
#include<vector>
#include<string>
#include<iostream>
#include <unistd.h>
#include <signal.h>

std::vector<long long> jobstack;
int num_of_swaps = 3;

void sig_alarm_handler(int signum)  {
	std::cout << "Connect Timeout" << std::endl ;
	exit(1);
}

void init() {
	setvbuf(stdout,0,2,0);
	signal(SIGALRM,sig_alarm_handler);
	alarm(60);
}


void menu() {
    std::cout << "1. Add task id to jobstack" << std::endl;
    std::cout << "2. Swap task ids in jobstack" << std::endl;
    std::cout << "3. Finish top task in jobstack" << std::endl;
    std::cout << "4. Quit. :pensive:" << std::endl;
    std::cout << "> ";
}

void print_all_task_ids()   {
    for (size_t i = 0; i < jobstack.size(); i++)
    {
        std::cout << "task " << i+1 << ": " << jobstack[i] << std::endl;
    }
}

int main(int argc, char const *argv[])
{
    init();
    int choice = -1;
    long long taskid = -1;
    int ind1, ind2;
    std::string employee_name, two_week_notice;
    std::cout << "Hi, this weird job you applied for wants you to complete tasks in a LIFO matter, sorry yeah but please dont quit. :pensive:" << std::endl;
    std::cout << "First off, what's your name?"  << std::endl;
    std::cout << "Employee name: ";
    std::cin >> employee_name;
    std::cout << "Hi " << employee_name << std::endl;
    jobstack.reserve(1001);

    while(1)    {
        menu();
        std::cin >> choice;
        switch(choice)  {
            case 1:
                if(jobstack.size() == 1000)  {
                    std::cout << "Im not a maniac, finish some tasks first mate you have too many" << std::endl;
                    break;
                }
                std::cout << "Enter task id: ";
                std::cin >> taskid;
                std::cout << "Added task id: " << taskid << " to your jobstack" << std::endl;
                jobstack.push_back(taskid);
                std::cout << "Added!" << std::endl;
                break;
            case 2:
                if(num_of_swaps == 0 || jobstack.size() < 2)
                    std::cout << "Not allowed" << std::endl;
                else    {
                    std::cout << "Dont do this very often..." << std::endl;
                    print_all_task_ids();
                    std::cout << "Enter indices:";
                    std::cin >> ind1 >> ind2;
                    if(ind1 > (int)jobstack.size() || ind2 > (int)jobstack.size())    {
                        std::cout << "Not allowed" << std::endl;
                        break;
                    }
                    std::swap(jobstack[ind1-1], jobstack[ind2-1]);
                    num_of_swaps--;
                    std::cout << "Swapped!" << std::endl;
                }
                break;
            case 3:
                if(jobstack.size() != 0)    {
                    std::cout << "Thanks, you finished task id:" << jobstack.back() << std::endl;
                    std::cout << "Now get back to work!!!" << std::endl;
                    jobstack.pop_back();
                }
                else    {
                    std::cout << "Wow your jobstack is empty... I must not be giving you enough work to do" << std::endl;
                }
                break;
            case 4:
                std::cout << "2 week notice: ";
                std::cin >> two_week_notice;
                exit(0);
            case 5:
                std::cout << "what?" << std::endl;
                break;
        }
    }
    

    
    return 0;
}
