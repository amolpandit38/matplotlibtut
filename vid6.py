import matplotlib.pyplot as plt

exp_vals = [1400, 600, 300, 410, 250]
exp_labels = ['Home rent', 'food', 'Phone/internet', 'car', 'other utilities']
plt.axis('equal')
plt.pie(exp_vals, labels=exp_labels, radius=1.5, autopct='%0.2f%%',
        explode=[0, 0, 0.2, 0, 0], startangle=45)

plt.savefig("pie_chart.png", bbox_inches='tight', pad_inches=2)
plt.savefig("pie_chart.pdf", bbox_inches='tight', pad_inches=2)
# saving chart files to local folder, or you can specify the path
plt.show()
