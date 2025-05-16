def myfunc():
    print("Hello world!")

myfunc()
print(__name__)   # if the file is run from here (it will print __main__)
                  # if it is imported somewhere and then if we ran that prog , it will print 'jay_module'


if __name__ == "__main__":         #this part wont run when the file is imported somewhere as __name__ becomes 'jay_module' (in that case)
    print("Here you can keep code which is runnable only if this file is directly excuted ---not when this is imported somewhere")
    print("special code")