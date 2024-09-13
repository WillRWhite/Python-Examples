class Myclass():


    def __init__(self,a:int) -> None:
        self.a = a

    def inc(self,x:int):
        return self.a + x
    

o = Myclass(3)
a = o.inc(2)
print(a)

