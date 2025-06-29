# Problem 3 - Matplotlib Scatterplot in Matplotlib ( https://www.geeksforgeeks.org/matplotlib-pyplot-scatter-in-python/)
import matplotlib.pyplot as plt
import numpy as np

x = np.array([12, 45, 7, 32, 89, 54, 23, 67, 14, 91])
y = np.array([99, 31, 72, 56, 19, 88, 43, 61, 35, 77])

plt.scatter(x, y)
plt.title("Basic Scatter Plot")
plt.xlabel("X Values")
plt.ylabel("Y Values")
plt.show()

x1 = np.array([160, 165, 170, 175, 180, 185, 190, 195, 200, 205])
y1 = np.array([55, 58, 60, 62, 64, 66, 68, 70, 72, 74])

x2 = np.array([150, 155, 160, 165, 170, 175, 180, 195, 200, 205])
y2 = np.array([50, 52, 54, 56, 58, 64, 66, 68, 70, 72])

plt.scatter(x1, y1, color='blue', label='Group 1')
plt.scatter(x2, y2, color='red', label='Group 2')

plt.xlabel('Height (cm)')
plt.ylabel('Weight (kg)')
plt.title('Comparison of Height vs Weight between two groups')
plt.legend()
plt.show()

x = np.array([3, 12, 9, 20, 5, 18, 22, 11, 27, 16])
y = np.array([95, 55, 63, 77, 89, 50, 41, 70, 58, 83])

a = [20, 50, 100, 200, 500, 1000, 60, 90, 150, 300] # size
b = ['red', 'green', 'blue', 'purple', 'orange', 'black', 'pink', 'brown', 'yellow', 'cyan'] # color

plt.scatter(x, y, s=a, c=b, alpha=0.6, edgecolors='w', linewidth=1)
plt.title("Scatter Plot with Varying Colors and Sizes")
plt.show()

x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]
sizes = [30, 80, 150, 200, 300]  # Bubble sizes

plt.scatter(x, y, s=sizes, alpha=0.5, edgecolors='blue', linewidths=2)
plt.title("Bubble Plot Example")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()

x = np.random.randint(50, 150, 100)
y = np.random.randint(50, 150, 100)
colors = np.random.rand(100)  # Random float values for color mapping
sizes = 20 * np.random.randint(10, 100, 100)

plt.scatter(x, y, c=colors, s=sizes, cmap='viridis', alpha=0.7)
plt.colorbar(label='Color scale')
plt.title("Scatter Plot with Colormap and Colorbar")
plt.show()

plt.scatter(x, y, marker='^', color='magenta', s=100, alpha=0.7)
plt.title("Scatter Plot with Triangle Markers")
plt.show()

