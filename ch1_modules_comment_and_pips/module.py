import pyjokes


joke = pyjokes.get_joke()
print("printing jokes-")     #prints line-1
print(joke)                  #prints in line-2

#if you want to keep it in line-1---do this    #single line comment

# u can use 'ctrl + /' to comment anything and uncomment anything....it is a vs code shortcut

""" 
this
is 
a 
multiline
comment
"""


'''
this
is 
also
a 
multiline
comment
'''



print("printing jokes-",end='')
print(joke) 