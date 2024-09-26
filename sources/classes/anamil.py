class Animal:

    # A single "_" in a variable name implies a private variable and should not be accessed directly from an objext
    # A double "__" is generally used for sub classes and the name is mangeled. See the link:
    # https://stackoverflow.com/questions/1301346/what-is-the-meaning-of-single-and-double-underscore-before-an-object-name
     
    def __init__(self, name=None, height=None, weight=None, sound=None) -> None:
    # __init__ is called when an objext is instanciated when the constructor is called  

        # __ means private. Can only access via a function within the class
        self._name = name
        self._height = height
        self._weight = weight
        self._sound = sound

    def __str__(self) -> str:
    # __str__ is called when the object is printed, so __str__ overloads the print() function
         return f" Animal = {self._name}, height = {self._height}, weight = {self._weight}"   
    
    def get_name(self) -> str:
    # Method to get a name since we should reframe fromn using obj._name
        return self._name
    
    def set_name(self, name) -> None:
    # Method to set a name since we should reframe fromn using obj._name
    # Should do a check to ensure name is valid
        self._name = name


    def make_noise(self) -> str:
        return(self._sound)
    

# Constructor for "cat"
cat = Animal("Silvesta", "1", "3", "meow")
# Constructor for "dog"
dog = Animal("Rover", "2", "5", "woff")


print(cat)
print(dog)

# This works but the point of the "-" is to tell the user no to do so

cat._name = "Puss in Boots"
print(cat._name)

# Instead should do this:



cat.set_name("Tiddles")
print(cat.get_name())

print(cat.make_noise())
print(dog.make_noise())