import matplotlib.pyplot as plt


def lmap(r,x):
    return r*x*(1-x)

r = 0.4
x = 0.5
N=[]
X=[]

for n in range(10):
    N.append(n)
    X.append(x)
    x = lmap(r,x)
print(N)
print(X)

# Plotting
plt.xlabel('n')
plt.ylabel('x')
plt.title("Logistic Map")
plt.grid(True)

plt.plot(N, X)
plt.show()
