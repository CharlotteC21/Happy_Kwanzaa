import numpy as np
import matplotlib.pyplot as plt

# create a dataset
height = [30, 30, 30, 40, 30, 30, 30]
bars = ('1', '2', '3', '4', '5', '6', '7')
x_pos = np.arange(len(bars))

# Create bars w/ diff colors
plt.bar(x_pos, height, color=['red', 'red', 'red', 'black', 'green', 'green', 'green'], edgecolor='blue')

# Create names on the x-axis
plt.xticks(x_pos, bars)
plt.title('Happy Kwanzaa!', fontsize=15)

# Show graph
plt.show()