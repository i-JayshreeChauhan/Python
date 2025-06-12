if __name__ == '__main__':

    l = []  #empty list

    for _ in range(int(input())):

        l1=[]  #empty lsit
        name = input()
        score = float(input())
        l1.append(name)
        l1.append(score)
        
        l.append(l1)

    #check for lowest and remove that
    #using enumerate to identify index and lowest marks

    lowest_marks = 101.0
    low_ind = 0 

    for index,i in enumerate(l):

        name,marks = i  #unpacking 
        if(marks<lowest_marks):
            lowest_marks = marks
            low_ind = index

    #remove lowest mark entries from list 

    while any(entry[1] == lowest_marks for entry in l):           #entry[1] --> sencond element of sublist
        for i, (name, number) in enumerate(l):
            if number == lowest_marks:
                l.pop(i)
                break  # break after removing one match to safely continue the loop

    #run the code again to identify lowest now
    lowest_marks = 101.0
    low_ind = 0 

    for index,i in enumerate(l):

        name,marks = i  #unpacking 
        if(marks<lowest_marks):
            lowest_marks = marks
            low_ind = index
    

    #make new list to save names having the lowest value 
    names_with_lowest_marks = []

    for name, number in l:
        if number == lowest_marks:
            names_with_lowest_marks.append(name)

    #sort the new list to make it lexicographical
    names_with_lowest_marks.sort()

    for i in names_with_lowest_marks:
        print(i)



    