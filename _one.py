def myFunc(int_in):
    return int_in/5


class myClass:
    oneval = 17
    def div(self, int_in):
        try:
            return int_in/self.oneval
        except TypeError:
            print("Must pass integer to div")
            return 0
        except:
            print("unknown error in div")
            return 0
    def __init__(self, inval): 
        self.oneval = inval


class newClass(myClass): 
    name = 'Levi'
    def __repr__(self):   
        name = "Jeff"
        return (self.name + ": oneval is equal to " +
                str(self.oneval))


C = myClass(4)      
B = myClass(10)
N = newClass(12)

print (N.div('rutebega'))
print(C)
print("Done~")
      
                 

if __name__ == "__main__":
    print(myFunc(21))
else:
    print("primer imported, not invoked")

