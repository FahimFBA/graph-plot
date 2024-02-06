# importing matplotlib
import matplotlib.pyplot as plt

# co-ordinates (2,2), (4, 6), (5,7), (7,10)
x = [2, 4, 5, 7]
y = [2, 6, 7, 10]

# plt the graph
plt.plot(x, y)

# label on the graph
plt.xlabel('X Axis')
plt.ylabel('Y Axis')

# Title for the plot/graph
plt.title('Graph Project using Python')

# save the graph/plot as a png file
plt.savefig('graph.png')

# show the plot/graph
plt.show()