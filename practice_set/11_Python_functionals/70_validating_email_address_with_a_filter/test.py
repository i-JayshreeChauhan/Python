        
s="hello@heaven.com"

a = s.find('@')
b = s.find('.')

print(a)
print(b)

un = s[:a]
ws = s[a+1:b]
ex = s[b+1:]

print(un)
print(ws)
print(ex)