"""
All type of 2D chart can be developed for data visualization
"""

import matplotlib.pyplot as plt

# in jupyter notebook you have to explicitly add magic '%matplotlib inline'

x = [1, 2, 3, 4, 5, 6, 7]
y = [50, 51, 52, 48, 47, 49, 46]
# path to api for plot in matplotlib "https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html"

# to plot the graph
plt.xlabel('Day')  # x-axis name
plt.ylabel('Temperature')  # y-axis name
plt.title('Weather')  # Title of the plot
plt.plot(x, y)  # it takes list as arguments
plt.show()  # this command enables the graph UI
