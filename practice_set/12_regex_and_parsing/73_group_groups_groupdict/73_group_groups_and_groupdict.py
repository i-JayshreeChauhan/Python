s = input()
for i in range(0,len(s)):
    if i != 0:   
        if s[i] == s[i-1] and s[i].isalnum():
            print(s[i])
            break
    
else:
    print(-1)
