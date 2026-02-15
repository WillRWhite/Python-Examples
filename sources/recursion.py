# https://gemini.google.com/share/181271a6f8c2

def draw(n:int) -> None:

    if n==0:
        return
    
    draw(n-1)

    for _ in range(n):
        print("#", end="")
    print()

def count(max_i:int, i:int=0) -> int:
    i+=1
    j:int=i
    if i==max_i:
        print("")
        return i
    else:
        print(f"{i}",end="")
        count(max_i,i)
        print(f"{j}",end="")
              

def sum_series(n: int) -> float:
    sum=0
    for x in range(1,n+1):
        sum = sum + 1/x**2
    return(sum)

def sum_series_recursive(n: int) -> float:
    # 1. Base Case: Stop when we hit the first term
    if n == 1:
        return 1.0
    
    # 2. Recursive Step: Current term + sum of all previous terms
    else:
        return (1 / n**2) + sum_series_recursive(n - 1)

def factorial(n):
    # 1. Base Case
    if n <= 1:
        return 1
    
    # 2. Recursive Step
    else:
        return n * factorial(n - 1)


def terminal(n: int) -> int:
    if n <= 1:
        return 1
    return n + terminal(n-1)


print(factorial(3))

print(terminal(4))

print(sum_series(998))

print(sum_series_recursive(998))


#count(10)

#print("")
#draw(5)
#print("")
#count(10)
#print("")


