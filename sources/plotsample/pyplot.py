import modules.plotmodules as pm

if __name__ == "__main__":

    debug = False

    # Define data

    plot_range = range(-11,11)

    a = 1
    b = 1
    c = -10

    x_values = [x for x in plot_range]
    y_values = [(a*x**2)+(b*x)+c for x in x_values]

    if debug:
        print(y_values)
        print(x_values)


    pm.plot_xy(x_values,y_values)




