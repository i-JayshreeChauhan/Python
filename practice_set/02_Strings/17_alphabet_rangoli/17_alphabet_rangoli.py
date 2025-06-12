
"""

#size 5

--------e--------
------e-d-e------
----e-d-c-d-e----
--e-d-c-b-c-d-e--
e-d-c-b-a-b-c-d-e
--e-d-c-b-c-d-e--
----e-d-c-d-e----
------e-d-e------
--------e--------

#size 3

----c----
--c-b-c--
c-b-a-b-c
--c-b-c--
----c----


"""

def print_rangoli(size):
    
    l=[] #empty list
    rl=[] #empty list
    k = size + 97 

    for i in range(97,k):
        rl.append(chr(i))
   
    
    l=rl.copy()
    rl.reverse()

    #print(l)
    #print(rl)

    #print("\n")



    column = ((size + (size-1)) * 2) - 1 
    width = column
    row = size + (size-1)

    #prepare pattern

    #top pattern 
    #l = ['a', 'b', 'c', 'd', 'e']
    #rl = ['e', 'd', 'c', 'b', 'a']

    for i in range(0,(row//2)):
        print("-".join(rl[:(i+1)] + l[len(l)-i:]).center(width,"-"))
        
    #middle pattern and bottom pattern

    for i in range(0,(row//2)+1):
        l.pop(0)
        print("-".join(rl+l).center(width,"-"))           
        length = len(rl)
        rl.pop(length-1)





if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)


