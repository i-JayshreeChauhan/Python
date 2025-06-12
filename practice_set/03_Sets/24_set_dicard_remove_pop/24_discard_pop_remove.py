n = int(input())
s = set(map(int, input().split()))

N = int(input())
for i in range (0,N):
    command = input().split()

    if len(command) == 2 :
        c = command[0]
        v = command[1]

        if(c=="discard"):
            s.discard(int(v))
        elif c=="remove":
            try:
                s.remove(int(v))
            except Exception as e:
                pass
    elif len(command) == 1 :
        c = command
        v = None

        try:
            s.pop()
        except Exception as e:
            pass

print(sum(s))