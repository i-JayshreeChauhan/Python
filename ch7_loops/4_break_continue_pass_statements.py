
#---------- BREAK statement

for i in range(10):
    print(i)
    if(i==7):
        break


print("----------------------")
#---------- CONTINUE statement

for i in range(10):
    if(i%3==0):
        continue
    print(i)


print("----------------------")
#---------- PASS statement

#pass is a null statement in python - it instructs to do nothing

for i in range(5):
    pass                #pass keyword will do nothing and allow interpreter to move forward

i=0
while i<3:
    print(i)
    i+=1