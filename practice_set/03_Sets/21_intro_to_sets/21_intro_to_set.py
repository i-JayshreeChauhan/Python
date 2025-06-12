def average(array):

    s = set()
    tot = 0
    
    for i in array:
        s.add(i)

    for i in s:
        tot += int(i)
    
    return format(float(tot/len(s)) , ".3f")


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)