import random
response = input("Enter your name: ")
print("Hello " + response + ", here are 5 random numbers")

for i in range(5):
    print(random.random())

print()
print("Thanks for running me!!")
print()
