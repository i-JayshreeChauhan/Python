from random import randint

guessed_number = randint(1,100)           #guesses number from 1 to 100
u_number = 0
count=0

while(guessed_number!=u_number):
    u_number = int(input("Enter Number : "))
    #print(f"User entered : {u_number}")
    
    if(u_number>guessed_number):
        print("try lower values")
    elif(u_number<guessed_number):
        print("try higher values")
    elif (u_number == guessed_number):
        print("---------------------------------")
        print(" ")
        print("You have guessed correct number!!")
        print(" ")
        print("---------------------------------")

    
    count +=1

print(f"total Guesses : {count}")
