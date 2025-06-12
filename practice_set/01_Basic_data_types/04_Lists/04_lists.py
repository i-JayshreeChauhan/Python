if __name__ == '__main__':
    N = int(input())
    l = []   # empty list

    for _ in range(N):

        data = input().split()

        if len(data)==3:
            string_part = data[0]
            position_part = int(data[1])
            number_part = int(data[2])
        elif len(data)==2:
            string_part = data[0]
            position_part = None
            number_part = int(data[1])
        elif len(data)==1:
            string_part = data[0]
            position_part = None
            number_part = None
        
        if(string_part.lower()=="insert"):
            l.insert(position_part,number_part) 
        elif(string_part.lower()=="print"):
            print(l)
        elif(string_part.lower()=="remove"):
            l.remove(number_part)
        elif(string_part.lower()=="append"):
            l.append(number_part)
        elif(string_part.lower()=="sort"):
            l.sort()
        elif(string_part.lower()=="pop"):
            l.pop(len(l)-1)  
        elif(string_part.lower()=="reverse"):
            l.reverse()          