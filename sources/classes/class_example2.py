class Temp:
    # note legacy declarations which have identical functionality in Python3:
    # class Temp()
    # class Temp(object)

    def __init__(self,temp_in:float) -> None:
       self.temp_in = temp_in

    def __str__(self) -> str:
        # Called by print(<instance>)
        return str(self.temp_in)
    
    def __repr__(self) -> str:
        # Called by repr(<instance>) or typing Temp() in an interactive Python shell
        # so to print you would need print(repr(<instance>))
        return (f"Temp(temp_in:float) -> None")
    
    def to_fh(self) -> float:
        return (self.temp_in*1.8 + 32)
    
    def to_cg(self) -> float:
        return(self.temp_in/1.8 - 32)
    
class Weight:

    def __init__(self,weight_in:float) -> None:
       self.weight_in = weight_in

    def __str__(self) -> str:
        return str(self.weight_in)
    
    def to_kg(self) -> float:
        return (self.weight_in*2.20462262185) 
    
    def to_lb(self) -> float:
        return(self.weight_in/2.204622 )

def main():

    temp:Temp = Temp(100.0)
    weight = Weight(25)

    # Use the __str__() method to print the value of the input variable
    print(temp)
    print(Temp(temp))
    print("repr")
    repr(Temp(temp))
    # So the above statement will give the same results as above
    print(temp.temp_in)

    # Call the two methods associated with any Temp instance
    print(temp.to_fh())
    print(temp.to_cg())

    print("Well, well)")
    print(Temp(temp))



    # Same again for the Weight class
    print(weight)
    print(weight.weight_in)
    print(weight.to_kg())
    print(weight.to_lb())

    # However the following will give errors

    #print(temp.to_kg())
    #print(weight.to_cg())


    print("int", temp.)

    

if __name__ == "__main__":
    main()



