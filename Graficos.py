import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Create a Tkinter window
root = tk.Tk()
root.title("Multiple Plots from CSV")

# Create a frame for the plots
frame = ttk.Frame(root)
frame.grid(row=0, column=0)

# Function to load data from CSV file
def load_data():
    data = pd.read_csv("Graficos\\Muestras.csv")
    update_plots(data)

def exit():   
    frame.destroy()
    root.destroy()

# Function to update all plots
def update_plots(data):
    # Clear existing plots
    for ax in axes:
        ax.clear()

    # Create new plots using data
    for i, col in enumerate(data.columns):
        ax = axes[i]
        ax.plot(data.index, data[col], label=col)
        ax.set_title(f"Entrada {i}")
        #ax.legend()

    canvas.draw()

# Button to load data and update plots
load_button = ttk.Button(root, text="Exit", command=exit)
load_button.grid(row=1, column=0, pady=10)

# Create 8 subplots
fig, axes = plt.subplots(4, 2, figsize=(10, 8), sharex=True)
axes = axes.flatten()

# Canvas widget to embed Matplotlib plots in Tkinter window
canvas = FigureCanvasTkAgg(fig, master=frame)
canvas_widget = canvas.get_tk_widget()
canvas_widget.grid(row=0, column=0)

load_data()

# Show the Tkinter window
root.mainloop()