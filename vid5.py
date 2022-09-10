import matplotlib.pyplot as plt

"""
in histogram there is a concept called bin and bucket - 
these are certainly ranges

by default it will plot 10 bins
bins = number of columns 
rwidth = separation between the bars
histtype = by default it is bar but you can set to step

bins can be specified in numbers or in a list
"""

blood_sugar = [113, 85, 90, 150, 149, 88, 93, 115, 135, 80, 77, 82, 129]
plt.hist(blood_sugar, bins=3, rwidth=0.95)
plt.hist(blood_sugar, bins=[80, 100, 125, 150], rwidth=0.95)
plt.hist(blood_sugar, bins=[80, 100, 125, 150], rwidth=0.95, histtype='step')
plt.show()

blood_sugar_men = [113, 85, 90, 150, 149, 88, 93, 115, 135, 80, 77, 82, 129]
blood_sugar_women = [67, 88, 93, 120, 115, 80, 90, 112, 150, 145, 78, 130, 135]
plt.xlabel('sugar range')
plt.ylabel('Total number of patients')
plt.title('Blood sugar analysis')
plt.hist([blood_sugar_men, blood_sugar_women], bins=[80, 100, 125, 150], rwidth=0.95,
         color=['green', 'orange'], label=['men', 'women'])
plt.legend()
plt.show()
