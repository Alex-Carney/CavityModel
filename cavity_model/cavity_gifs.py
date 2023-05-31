import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from IPython.display import Image

def create_gif(x_data, y_data_list, gammas, xlabel, ylabel, base_title, filename, interval=200):
    """
    Create a GIF of plots with the same X-axis and changing Y-axis.

    Parameters:
    x_data (array-like): X-axis data
    y_data_list (list of array-like): List of Y-axis data for each frame
    gammas (list of float): List of gamma values for each frame
    xlabel (str): Label for the X-axis
    ylabel (str): Label for the Y-axis
    base_title (str): Base title for the plot
    filename (str): Filename for the output GIF
    interval (int, optional): Time between frames in milliseconds. Default is 200ms.
    """

    # Set up the plot
    fig, ax = plt.subplots()
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    line, = ax.plot(x_data, y_data_list[0])
    title_text = ax.text(0.5, 1.05, base_title, transform=ax.transAxes, ha="center")

    # Update function for the animation
    def update(frame):
        line.set_ydata(y_data_list[frame])
        ax.set_ylim(np.min(y_data_list[frame]), np.max(y_data_list[frame]))
        title_text.set_text(f"{base_title} Phi = {gammas[frame]:.2f}")
        return line, title_text

    # Create the animation
    ani = FuncAnimation(fig, update, frames=len(y_data_list), interval=interval, blit=True)

    # Save the animation as a GIF
    ani.save(filename, writer='pillow')

    # Display the saved GIF in Jupyter Notebook (optional)
    return Image(filename=filename)
