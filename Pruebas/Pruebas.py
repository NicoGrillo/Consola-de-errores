import matplotlib.pyplot as plt
import numpy as np

# Sample data
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Create the initial line plot
line, = plt.plot(x, y, label='Sin(x)')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.legend()

# Function to update the line plot
def update_plot():
    # Generate new data or modify existing data
    new_y = np.cos(x)

    # Update the y-data of the line plot
    line.set_ydata(new_y)

    # Redraw the plot
    plt.draw()

# Show the initial plot
plt.show()

# Optionally, you can repeatedly call the update_plot function to refresh the plot
# For example, simulate real-time updates with a loop
for _ in range(10):
    update_plot()
    plt.pause(1)  # Pause for 1 second (adjust as needed)