class Temp:
    def __str__(self):
        return "User-friendly string"

    def __repr__(self):
        return "Temp()"

class Test:
    # The following are class variables
    a:int = 0
    b:float = 0

    #def __init__(self, c:int, name:str) -> None:
    #    # # This is an instance variable
    #    self.c = c
    #    self._name = name

    def __init__(self, c:int) -> None:
        # # This is an instance variable
        self.c = c
        # The following is a "private" instance variable
        # Although will "show up" in intellisense and is 
        # selectable the underscore is an indication to the
        # user that they should not select it but use the
        # @property method instead. The @property decorator
        # gives access to this variable as an attribute/property
        self._name = "Doggy"

    @property
    def name(self):
        # Getter method: Called when accessing self.name
        return self._name

    @name.setter
    def name(self, new_name):
        # Setter method: Called when assigning a value to self.name
        if isinstance(new_name, str):
            self._name = new_name
        else:
            raise ValueError("Name must be a string")

class Dog:
    def __init__(self, name):
        self._name = name  # Private instance variable

    @property
    def name(self):
        # Getter method: Called when accessing self.name
        return self._name

    @name.setter
    def name(self, new_name):
        # Setter method: Called when assigning a value to self.name
        if isinstance(new_name, str):
            self._name = new_name
        else:
            raise ValueError("Name must be a string")



dog = Dog("Fido")
print(dog.name)  # Calls the getter: Output is "Fido"
dog.name = "Buddy"  # Calls the setter to update the name
print(dog.name)  # Output is "Buddy"

t = Test(3)
print(t.name)
t.name = "Scooby"
print(t.name)

# You shouldn't do this _name is a variable
# the correct way to do this is via the setter method
# t.name
t._name = "Stanley"
print(t._name)



t = Temp()

print(Temp())
print(repr(Temp()))

print(t)
print(repr(t))

