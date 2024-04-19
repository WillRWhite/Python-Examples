import matplotlib.pyplot as plt

def main() -> None:

##### Program Constants #####    
    Max_N = 10
    r = 0.4
    x = 0.5
#############################

    n_list=[]
    x_list=[]

    for n in range(Max_N):
        n_list.append(n)
        x_list.append(x)
        x = lmap(r,x)
    # print(n_list)
    # print(x_list)

    plotResults(n_list, x_list, title="Logistic Map", x_label="Iteration", y_label="x data")


def lmap(r: float, x: float) -> float:
    return r*x*(1-x)

def plotResults(x_data: list, y_data: list, x_label: str, y_label: str, title: str) -> None:
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)
    plt.grid(True)

    plt.plot(x_data, y_data)
    plt.show()


if __name__ == "__main__":
    main()

