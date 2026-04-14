import matplotlib.pyplot as plt

def plot_xy(x_list: list, y_list: list) -> None:
    # 1 Create the plot
    plt.plot(x_list, y_list)

    # 2 Adjust the spines to intersect at (0,0)
    ax = plt.gca()

    # Move the left and bottom spines to the zero position
    ax.spines['left'].set_position('zero')
    ax.spines['bottom'].set_position('zero')

    # Hide the top and right "box" lines
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')

    # Ensure the view includes 0 even if the data is high up
    # We use a little padding (e.g., -10) so the axis line isn't cut off
    plt.ylim(bottom=min(0, min(y_list)) - 10, top=max(y_list) + 10)
    plt.xlim(left=min(0, min(x_list)) - 2, right=max(x_list) + 2)

    # 3 Add labels and a title
    # 'loc' helps position the labels at the ends of the axes
    plt.xlabel('x-axis', loc='right')
    plt.ylabel('y-axis', loc='top')
    plt.title('Basic X-Y Plot with Origin at (0,0)')

    # Optional: Add a grid to make the origin easier to spot
    plt.grid(True, linestyle=':', alpha=0.6)

    # 4. Display the plot
    plt.show()


if __name__ == "__main__":

    # Define data

    plot_range = range(-11,11)

    a = 1
    b = 1
    c = -10

    x_values = [x for x in plot_range]
    y_values = [(a*x**2)+(b*x)+c for x in x_values]

    plot_xy(x_values, y_values)
