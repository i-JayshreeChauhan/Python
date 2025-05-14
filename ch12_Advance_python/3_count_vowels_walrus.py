
"""
Count vowels in input until user enters "stop"  using walrus operator

--Keep asking the user to enter a word.
--For each word, print how many vowels it contains.
--Stop when the user types "stop" (case-insensitive).

"""
count=0

while (ip := input("Enter word : ").lower()) != "stop":           #explaination (take input in ip and if not equal to stop go into the loop)
    for k in ip:
        if(k=='a' or k=='e' or k=='i' or k=='o' or k=='u'):
            count+=1
    else:
        print(f"total vowels in {ip} is = {count} ")
        count=0

print("Program ended!")

