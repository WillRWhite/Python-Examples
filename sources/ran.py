import random
yourName = input("Enter your name: ")
yourAge = input("How old are you: ")

if int(yourAge) > 50:
    age = "old"
else:
    age = "young"

print("Hello " + yourName + ". Wow you are " + age + ". Here are 5 random numbers")

for i in range(5):
    print(random.random())

print()W
print("Thanks for running me!!")
print()
