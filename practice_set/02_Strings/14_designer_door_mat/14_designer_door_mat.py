dash = "-"
design = ".|."
welcome = "WELCOME"

row , column = (input().split())   
row = int(row) 
column = int(column)


"""
 Size: 11 x 33
 ---------------.|.---------------
 ------------.|..|..|.------------
 ---------.|..|..|..|..|.---------
 ------.|..|..|..|..|..|..|.------
 ---.|..|..|..|..|..|..|..|..|.---
 -------------WELCOME-------------
 ---.|..|..|..|..|..|..|..|..|.---
 ------.|..|..|..|..|..|..|.------
 ---------.|..|..|..|..|.---------
 ------------.|..|..|.------------
 ---------------.|.---------------



"""

halfrange = row//2 

# here Arithmatic progression 1,3,5,7,9,11,....
# difference = d = 2
# a = 1 (starting value)
# nth term = a + (n-1)*d
# example 5th term = 1 +(4)*2 = 9
#using this logic to find pattern size 



for i in range(1,row+1):

    if i <= halfrange :
        a = 1 
        loop = a + ((i-1) * 2)            # nth term = a + (n-1)*d
        design_pattern_size = loop * len(design)
        dash_pattern_size = (column - design_pattern_size) / 2

        print(dash* int(dash_pattern_size) , end="")
        print(design*loop , end="")
        print(dash*int(dash_pattern_size))

       

    elif i==(halfrange+1):
        design_pattern_size = len(welcome)
        dash_pattern_size = (column - design_pattern_size) / 2

        print(dash*int(dash_pattern_size) , end="")
        print(welcome , end="")
        print(dash*int(dash_pattern_size))

    elif i > (halfrange+1):
        n = (row - i + 1)
        loop = a + ((n-1) * 2)            # nth term = a + (n-1)*d
        design_pattern_size = loop * len(design)
        dash_pattern_size = (column - design_pattern_size) / 2

        print(dash* int(dash_pattern_size) , end="")
        print(design*loop , end="")
        print(dash*int(dash_pattern_size))


