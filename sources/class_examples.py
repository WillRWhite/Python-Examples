class Myclass:
    # Ref: https://chatgpt.com/c/66e41f81-1524-8004-9ff3-67e8bab90dd2
    # Atibute (var) not in __init__ method,therefore  has to be initilised in the class
    # Such attributes are reffered to as class attributes. They will also be available
    # in an instanciated object which is constructed by __new__() followed by __init__
    var:int = 0
 
    def __init__(self, a:int, b:int=1,) -> None:
    # Attribute (self.a) can be passed as a parameter to the class and initilised 
    # by the __init__ method. Such attributes are referred to as instance attributes
    # Although the __init__ method can be loosely referred
    # to as the constructor it actually is not, since it does not create the object
    # it mearly initilises an object attributes, if required. The constructor is 
    # automatic on instanciation but can be overloaded in the class by calling
    # __new__()
        self.a = a
        self.b = b

    def inc(self,x:int) -> int:
        #-1 return self.a + x
        self.a = self.a + self.b + x
        pass
        return self.a #-1 Not required but just here because function
                 #-1  definition defines a return value
    
    # The following function is only available for use within the class
    def inc2(x):
        return x + 1
    
    def inc3(x):
        x = vars
        return x
    
    var = inc2(5)

def main():
    pass
    print("Myclass =", Myclass.var)
    Myclass.var = 7

    o1 = Myclass(3)
    print("o1 =", o1.var, Myclass.var, o1.a, o1.b)

    o2 =Myclass(2,4)
    print("o2 =", o2.var, Myclass.var, o2.a, o2.b)

    o1.var = 3
    print("o1 =", o1.var, Myclass.var, o1.a, o1.b)

    o2.var = 5
    print("o2 =", o2.var, Myclass.var, o2.a, o2.b)


    #-1 a = o.inc(2)
    #-1 print(a)

    o1.inc(2)
    print("o1 =", o1.var, o1.a, o1.b)

    o2.inc(3)
    print("o2 =", o2.var, o2.a, o2.b)



    # Example on "no-op" statements in Python

    # This one actually does something but has no effect
    print("",end="")

    # Proper no-ops:
    pass
    ...
    None

if __name__ == "__main__":
    main()