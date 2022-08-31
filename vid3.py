import matplotlib.pyplot as plt

# axes labels, legends, grid

days = [1, 2, 3, 4, 5, 6, 7]
max_t = [50, 51, 52, 48, 47, 49, 46]
min_t = [43, 42, 40, 44, 33, 35, 37]
avg_t = [45, 48, 48, 46, 40, 42, 41]

plt.xlabel("Days")
plt.ylabel("Temperature")
plt.title("weather")
plt.plot(days, max_t, label="Max")
plt.plot(days, min_t, label="Min")
plt.plot(days, avg_t, label="Average")
plt.legend(loc="best",
           shadow="true")  # lower right, upper right # best is for auto-detect where to place the legend on the GUI

plt.grid()  # with grid, we can easily figure out the values on the plot,less eye job 
plt.show()
