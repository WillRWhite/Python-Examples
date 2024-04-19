def lmap(r,x):
    return r*x*(1-x)

r = 0.4
x = 0.5

for n in range(9):
    print(x)
    x = lmap(r,x)
