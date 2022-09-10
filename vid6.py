import matplotlib.pyplot as plt

exp_vals = [1400, 600, 300, 410, 250]
exp_labels = ['Home rent', 'food', 'Phone/internet', 'car', 'other utilities']
plt.axis('equal')
plt.pie(exp_vals, labels=exp_labels, radius=1.5, autopct='%0.2f%%',
        explode=[0, 0, 0.2, 0, 0], startangle=45)
plt.show()
