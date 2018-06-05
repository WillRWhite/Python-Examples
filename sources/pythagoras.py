import math

print("Calculate the unkown side of a right angle triangle.")
print("Enter 0 (zero) for the unknown side.")
print()
h = int(input("What is the lenght of the hypotenuse: "))
o = int(input("What is the lenght of the oposite side: "))
b = int(input("What is the lenght of the base: "))
print()

if (h == 0):
    h = math.sqrt(o**2 + b**2)
    print("The hypotenuse is: " + str(h))
elif (o == 0):
    o = math.sqrt(h**2 - b**2)
    print("The opposite is: " + str(o))
elif (b == 0):
    b = math.sqrt(h**2 - o**2)
    print("The base is: " + str(b))
else:
    print("One side must be unknown. Try again")
