
class Train:
    seats=0    #shared static variable

    @staticmethod
    def booktickets():
          Train.seats +=1
    
    @staticmethod
    def getstatus():
         return Train.seats
    
    @staticmethod
    def getfair():
         return 100
    

t1 = Train()
t1.booktickets()
t1.booktickets()

print(t1.getstatus())    # answer : 2

t2 = Train()
t2.booktickets()
t2.booktickets()

print(t2.getstatus())     # answer : 4    (if you would hve used t1.status()---it would have been the same)

print(t1.getfair())