from xmlrpc.client import Boolean


print("Welcome to the Seamulator!\n")
print("~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~")
print("~~~~~~~~~~~~~~~~~~~~~~~~~  /`·.¸   ~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("~~~~~~~~~~~~~~~~~~~~~~~~  /¸...¸`:·   ~~~~~~~~~~~~~~~~~~~~~~~")
print("~~~~~~~~~~~~~~~~~~~~~ ¸.·´  ¸   `·.¸.·´) ~~~~~~~~~~~~~~~~~~~~")
print("~~~~~~~~~~~~~~~~~~~~ : o ):´;      ¸  { ~~~~~~~~~~~~~~~~~~~~~")
print("~~~~~~~~~~~~~~~~~~~~~ `·.¸ `·  ¸.·´\\`·¸) ~~~~~~~~~~~~~~~~~~~~")
print("~~~~~~~~~~~~~~~~~~~~~~~   `\\\\´´\\¸.·´  ~~~~~~~~~~~~~~~~~~~~~~~")
print("~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~\n")
exit = False
coin = 1
action = []
        
def checkCoin (coin):
    print("Your coin now is : $" + str(coin) + "\n")

def checkAction():
    if (len(action) == 7):
        print("Nice! Here is the flag : COMPFEST14{l3ts_s4v3_0ur_f1sh_oN_th3_0ce4n}")
    else:
        print("That's not the right action.\n")

while (not exit) :
    print("Menu :")
    print(" 1. Check coin \n 2. Swim \n 3. Eat another fish \n 4. Jump \n 5. Check Action \n 6. Exit")
    i = int(input("Choose one : "))

    if (i==1):
        checkCoin(coin)
    elif (i==2):
        coin *= 10
        action.append("S")
        print("Your fish has been swim!\n")
    elif (i==3):
        coin += 12
        action.append("E")
        print("Your fish has been eat!\n")
    elif (i==4):
        coin *= 2
        action.append("J")
        print("Your fish has been jump!\n")
    elif (i==5):
        checkAction()
    elif (i==6):
        exit = True
        quit()
    else :
        print("There is no action for that.")
