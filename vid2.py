from matplotlib import pyplot as plt

x = [1, 2, 3, 4, 5, 6, 7]
y = [50, 51, 52, 48, 47, 49, 46]
# path to api for plot in matplotlib "https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html"

# to plot the graph
plt.xlabel('Day')  # x-axis name
plt.ylabel('Temperature')  # y-axis name
plt.title('Weather')  # Title of the plot
plt.plot(x, y, 'g*--')  # format strings in plot function
# here g is for green, * is for plot, -- is for type of graph
# the order doesn't matter it can work same for '--*g'

# it is same as keyword argument
plt.plot(x, y, color="red", marker="*", linestyle="--")
plt.show()
