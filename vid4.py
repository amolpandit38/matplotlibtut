import matplotlib.pyplot as plt
import numpy as np

company = ['GOOGLE', 'AMZN', 'MSFT', 'META']
revenue = [90, 136, 89, 27]
profit = [40, 2, 34, 12]

xPos = np.arange(len(company))
print(xPos)

plt.xticks(xPos, company)


plt.bar(xPos+0.2, revenue, width=0.4, label="Revenue")  # here new array will be created
plt.bar(xPos-0.2, profit, width=0.4, label="Profits")  # for horizontal chart use "barh"
plt.xlabel("Companies")
plt.ylabel("Revenue")
plt.title("US Tech Stocks")

plt.legend()
plt.ylabel("Revenue")
plt.show()
