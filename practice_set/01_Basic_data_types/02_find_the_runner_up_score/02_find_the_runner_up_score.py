

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

    l1 = list(arr)

    max_num = max(l1)
    while max_num in l1:
        l1.remove(max_num)

    #now we are left with list without the max number and we can identify the runner up
    max_num = max(l1)
    print(max_num)

