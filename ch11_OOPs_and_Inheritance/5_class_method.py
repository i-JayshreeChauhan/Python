
class Employee:
    id=10

    @staticmethod
    def show():
        print(f"The id value is {Employee.id}")   #accessing class attribute eevry time

    #other way to access class attribute everytime is classmethod decorator

    @classmethod
    def show1(cls):
        print(f"The id value is {cls.id}")



e = Employee()
e.id = 55
e.show()
e.show1()