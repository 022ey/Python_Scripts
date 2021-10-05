import random

a=int(input("Enter the stating range of the number : "))
b=int(input("Enter the Ending range of the number : "))

x = random.randint(a,b)

print("")
y=int(input("The Correct Number is : "))
t=0
while(t==0):
    y=int(input("The Correct Number is : "))
    if(x<y):
        print("")
        print("oops! wrong number")
        print("Here's a hint (The number is less than the number you have guessed)")

    if(x>y):
        print("")
        print("oops! wrong number")
        print("Here's a hint (The number is greater than the number you have guessed)") 

    if(x==y):
        print("")
        print("Yay! You have won")
        print("You guessed the correct number")
        t=1