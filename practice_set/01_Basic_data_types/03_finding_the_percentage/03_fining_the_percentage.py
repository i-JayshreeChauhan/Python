

if __name__ == '__main__':

    n = int(input())
    student_marks = {}   #empty dictionary

    #The underscore _ is a convention in Python used when you don’t care about the loop variable.
    #It means: "I’m looping n times, but I don’t need the index value."

    for _ in range(n):  
        name, *line = input().split() 
        scores = list(map(float, line))   # map float function Converts ['90', '85', '88'] to [90.0, 85.0, 88.0]
        student_marks[name] = scores
    query_name = input()

    l1 = student_marks[query_name]
    val = round( float(sum(l1[:3])) / 3.0 , 2)  #takes max upto 3 list values

    print(f"{val:.2f}")

