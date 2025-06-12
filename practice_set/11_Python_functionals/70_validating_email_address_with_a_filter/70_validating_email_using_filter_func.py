def fun(s):

    """
    #valid email checker

    - It must have the username@websitename.extension format type.
    - The username can only contain letters [a-z][A-Z], digits [0-9], dashes [-] and underscores [_] .
    - The website name can only have letters and digits [a-z][A-Z] and [0-9]
    - The extension can only contain letters [a-z][A-Z]
    - The maximum length of the extension is 3
    """
    try:
        a = s.find('@')
        b = s.find('.')

        un = s[:a]
        ws = s[a+1:b]
        ex = s[b+1:]

        if len(un)==0 or len(ws)==0 or len(ex)==0:
            return False

        if a == -1 or b == -1 or b < a:
            return False

        if not all(c.isalnum() or c in '-_' for c in un):
            return False
        
        if not all(c.isalnum() for c in ws) :
            return False
        
        if not (ex.isalpha() and len(ex) <= 3) :
            return False

        return True
    
        #print(un)
        #print(ws)
        #print(ex)

    except:
          return False




def filter_mail(emails):
    return list(filter(fun, emails))

if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())


filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)