import random
import datetime

def search1(list):
    start = datetime.datetime.now()
    print(f"Start time of search1() function = {start}" )
    for indx in range(n):
          if list[indx] == 1:
               print(f"Found 1 at index {indx}") 
               stop = datetime.datetime.now()
               print(f"Stop time of search1() function  = {stop}")
               seconds = (stop-start).total_seconds()
               print(f"Time taken to complete search = {seconds}")
               break           

# Size of list is n:
n = 100000000

# Generates a random number between 0 and n
r = random.randint(0, n)
print(f"Random number between 0 and {n} is {r}. This is the number the search1() function is looking for.")

# Create list with index [0] to [n-1]
print(f"Create list with {n} elements")
zeros_list = [0 for i in range(n)]

# Change the r index to 1. r is secret
zeros_list[r] = 1
print("End create list")

# Run the find_1() function to find at which index is the 1
search1(zeros_list)
