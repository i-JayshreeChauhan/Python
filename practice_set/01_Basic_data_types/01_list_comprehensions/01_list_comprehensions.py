
def checksum(l:list,n:int) -> bool :
    s = sum(l[:3])  #till the 3rd element (0,1,2 not 3rd)
    if(s!=n):
        return True
    return False


if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())


    xl = [ i for i in range(x+1) ]
    #print(xl)

    yl = [ i for i in range(y+1) ]
    #print(yl)

    zl = [ i for i in range(z+1) ]
    #print(zl)


    l1 = [[i,j,k] for i in xl  for j in yl  for k in zl]   #getting all permutations
    #print(l1)


    # we will use filter inorder to check which list has sum < n 
    l2 = filter(lambda subl : checksum(subl,n) , l1 )
    print(list(l2))




