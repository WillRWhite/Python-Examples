import matplotlib.pyplot as plt


def lmap(r,x):
    return r*x*(1-x)

r = 0.4
x = 0.5
N=[]
X=[]

for n in range(20):
    N.append(n)
    X.append(x)
    x = lmap(r,x)
print(N)
print(X)

plt.plot(X, N)
plt.show()
