import random
def check(a,b):
    if(x==y):
        print("Wow What a coincidence you both picked the same one try again Hope you may Win next time")

    if(x==1 and y==2):
        print("Oops You've Lost.. The system chose Rock and you chose Paper...   Try Again....")

    if(x==1 and y==3):
        print("Yay! You've Won The system chose Rock and you chose Scissors")

    if(x==2 and y==3):
        print("Oops You've Lost.. The system chose Scissors and you chose Paper...   Try Again....")

    if(y==1 and x==2):
        print("Yay! You've Won The system chose Rock and you chose Paper")

    if(y==1 and x==3):
        print("Oops You've Lost.. The system chose Rock and you chose Scissors...   Try Again....")

    if(y==2 and x==3):
        print("Yay! You've Won The system chose Paper and you chose Scissors")

t=1
while(t==1):
    print("")
    print("Enter 1 if you want to choose Rock")
    print("Entet 2 if you want to choose Paper")
    print("Enter 3 if you want to choose Scissors")

    print("")
    x=int(input("Rock - Paper - Scissors : "))
    print("")
    y=random.randint(1,3)

    check(x,y)
    t=int(input("Enter 0 if you want to quit or Enter 1 if you wish to continue : "))
