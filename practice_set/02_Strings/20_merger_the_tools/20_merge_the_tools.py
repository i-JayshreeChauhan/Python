def merge_the_tools(string, k):
    l1 =[]   #empty list  
    
    l1 = [string[i:i+k] for i in range(0,len(string),k)]
    #print(l1)

    for i in l1:
        s = set() #empty set
        l2 = []  #empty list
        for char in i:
            if char not in s:
                s.add(char)
                l2.append(char)
            str = "".join(l2)
        print(str)
    
            

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)