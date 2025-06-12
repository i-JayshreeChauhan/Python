from collections import deque

N = int(input())
d = deque()

for i in range(N):
    command = input().split()
    if len(command) == 1:
        com = command[0]
        value = None
    elif len(command)==2:
        com = command[0]
        value = int(command[1])

    if com == 'append':
        d.append(value)
    elif com == 'appendleft':
        d.appendleft(value)
    elif com == 'pop':
        d.pop()
    elif com == 'popleft':
        d.popleft()
    else:
        pass

for i in d:
    print(i,end=" ")
