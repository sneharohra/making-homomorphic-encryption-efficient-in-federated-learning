# import matplotlib.pyplot as plt
#
# # Define the data for the two line graphs
# x_values = [1, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30]
# y1_values = [2.475800067186355591e-01,
# 3.415400075912475586e-01,
# 3.849400067329406738e-01,
# 4.008400144577026367e-01,
# 4.154000020027160645e-01,
# 4.310399980545043945e-01,
# 4.44399976253509521e-01,
# 4.548200073242187500e-01,
# 4.618599972724914551e-01,
# 4.664599857330322266e-01,
# 4.724599857330322266e-01]
# y2_values = [2.675800067186355591e-01,
# 3.515400075912475586e-01,
# 3.949400067329406738e-01,
# 4.118400144577026367e-01,
# 4.214000020027160645e-01,
# 4.380399980545043945e-01,
# 4.5399976253509521e-01,
# 4.658200073242187500e-01,
# 4.748599972724914551e-01,
# 4.814599857330322266e-01,
# 4.864599857330322266e-01]
#
# # Create a new figure and axis object
# fig, ax = plt.subplots()
#
# # Plot the first line graph
# ax.plot(x_values, y1_values, label='w/o QAT and Clipping')
#
# # Plot the second line graph
# ax.plot(x_values, y2_values, label='QAT and Clipping')
#
# ax.set_xlabel('Epochs')
# ax.set_ylabel('Accuracy')
#
# ax.legend()
#
# # Add a title and legend
# ax.set_title('cifar10 Performance')
#
# # Display the plot
# plt.show()

import matplotlib.pyplot as plt

# Define the data for the bar graph
import numpy as np

x = np.array(["fashionMNIST", "Cifar10"])
y1 = np.array([421, 2460])
y2 = np.array([211, 1854])

x_numeric = np.arange(len(x))

bar_width = 0.35

# Create the figure and axes objects
fig, ax = plt.subplots()

# Plot the first bar chart
ax.bar(x_numeric - bar_width/2, y1, bar_width, label='w/o QAT and Clipping')

# Plot the second bar chart
ax.bar(x_numeric + bar_width/2, y2, bar_width, label='QAT and Clipping')


# Set the labels and title
ax.set_ylabel('Time (Seconds)')
ax.legend()

# Display the plot
plt.show()

