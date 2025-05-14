import random

def game():
    a = random.randint(1,50)     #returns random number between 1 to 50
    return a


value = game()
print(f"results are : {value}")

with open("D:\\0___LEARN\\Python\\ch9_File_io\\Practice_set\\game_results.txt" , "r+" ) as f:   
    read_data = f.read()
    if(len(read_data)==0):
        f.seek(0) #Move to start
        f.write(str(value)) #Overwrite
        f.truncate()  # Remove leftover text
    elif(int(read_data) < value):
        print("You have set a new Record ! congratulation !!")
        f.seek(0) #Move to start
        f.write(str(value))
        f.truncate()  # Remove leftover text
    elif(int(read_data) > value):
        print("Better luck next time!")
        print(f"High score = {int(read_data)}")
    else:
        pass 