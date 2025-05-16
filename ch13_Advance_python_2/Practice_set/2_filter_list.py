l = [1,4,55,2,30,6,7,80,50]

#filter this list based on value diviible by 5
def div (n:int) -> bool:
    if(n%5==0):
        return True
    return False

l1 = filter(div,l)
print(list(l1))