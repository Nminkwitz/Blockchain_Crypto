def myFunc(int_in):
    return int_in/5

print("Hello!")

# Class - a way to collect together both functions and data. You can also different instances of the same class that have different data inside
class myClass:
    oneval = 17
    def div(self, int_in): # int_in --> takes an integer in
        return int_in/self.oneval
    def __init__(self, inval): 
        self.oneval = inval


class newClass(myClass): # inherits from myClass
    name = 'Levi'
    def __repr__(self):   # representation built in fn -
        name = "Jeff"
        return (self.name + ": oneval is equal to " +
                str(self.oneval))

# instance of this class
C = myClass(4)      # its gonna make a brand new class instance, pass it as self, then pass inval as 4
B = myClass(10)
print(C.oneval)     # specify that you mean the oneval inside the specific instance of my class called C
print(C.div(34))    # if you want to invoke it with the C.div
print(B.div(34))

N = newClass(12)
print(N.name)
print(N.div(36))    # got 3 cuz we divided the 36 by the oneval that lives inside the new instance N which = 12
print(N)

                    # if you try to print C.name --> there will be an error. Its gonna say wait myClass doesnt have any name
                    # newClass inherits the functionality of myClass, by myClass cant use the functionality of newClass

if __name__ == "__main__":
    print(myFunc(21))
else:
    print("primer imported, not invoked")

