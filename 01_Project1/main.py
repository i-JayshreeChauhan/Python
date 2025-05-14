
#develop a game of Rock,paper,scissors !


import random

computer_val = random.choice([1,2,3])

user = input("Enter your choice (R,P,S) : ")
d1 = { "R" : 1 , "P" : 2 , "S" : 3 }
inv_d1 = {  1 : "Rock"  , 2 : "Paper"  , 3 : "Scissors" }
user_val = d1[user]

print(f"Computer chose {inv_d1[computer_val]} and You chose {inv_d1[user_val]}")

if(computer_val==user_val):
    print("It is a Tie")
elif(computer_val==1 and user_val==2):
    print("You Win!")
elif(computer_val==1 and user_val==3):
    print("You Lose!")
elif(computer_val==2 and user_val==1):
    print("You Lose!")
elif(computer_val==2 and user_val==3):
    print("You Win!")
elif(computer_val==3 and user_val==1):
    print("You Win!")
elif(computer_val==3 and user_val==2):
    print("You Lose!")
else:
    pass

