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
              
print("")
draw(5)
print("")
count(10)
print("")
