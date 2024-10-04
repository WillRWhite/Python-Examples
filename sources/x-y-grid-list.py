def grid():
    # Example list as a 2d grid using a list comprehension.
    # Each grid location is represented as a tuple (x,y)
    mylist = [[(x,y) for x in range(x_max+1)] for y in range(y_max+1)]
    return mylist

def print_grid_neg_y():
    # Print y-axis increasing downwards
    for x in range(y_max+1):
        for y in range(x_max+1):
            print(mylist[x][y], end=" ")
        print("")

def print_grid_pos_y():
    # Print y-axis increasing upwards
    for x in range(y_max,-1,-1):
        for y in range(x_max+1):
            print(mylist[x][y], end=" ")
        print("")


if __name__ == "__main__":

    DEBUG = False
    x_max = 4
    y_max = 8
    
    mylist = grid()

    if DEBUG:
        print("")
        print(mylist)
        print("")

    print("")
    print_grid_neg_y()
    print("")
    print_grid_pos_y()
