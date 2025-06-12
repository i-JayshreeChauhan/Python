def print_formatted(number):


    width = len(bin(number)[2:])  # Set width based on binary length 

    for i in range(1,number+1):
        print(str(i).rjust(width),end=" ")
        print(str(oct(i).upper()[2:]).rjust(width),end=" ")
        print(str(hex(i).upper()[2:]).rjust(width),end=" ")
        print(str(bin(i)[2:]).rjust(width))
 
if __name__ == '__main__':
    n = int(input())
    print_formatted(n)