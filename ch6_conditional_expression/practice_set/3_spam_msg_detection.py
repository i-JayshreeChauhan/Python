
a = input("Enter msg : ")

if (a.find("make a lot of money")) != -1 :
    print("----- IT IS A SPAM MSG -----")
elif (a.find("buy now")) != -1 :
    print("----- IT IS A SPAM MSG -----")
elif (a.find("subscribe this")) != -1 :
    print("----- IT IS A SPAM MSG -----")
elif (a.find("click this")) != -1 :
    print("----- IT IS A SPAM MSG -----")
else:
    print("--MSG OK--")