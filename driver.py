#Driver script

import os
import numpy as np
import matplotlib.pyplot as plt
from src.linalg_interp import cubic_spline

def load_data(file_path):

    # Loading data from file
    with open (file_path) as f:
        delimiter = ',' if ',' in f.readline() else '\t'
    return np.loadtxt(file_path, delimiter=delimiter)

def generate_spline_plot(xd, yd, title, output_file):

    # Function to generate spline functions and save to file.
    
    orders = [3]
    x_new = np.linspace(xd[0], xd[-1], 100)
   

    fig, axs = plt.subplots(len(orders), 1, figsize=(12, 4 * len(orders)))
    if len(orders) == 1:
        axs = [axs]



    for i, order in enumerate(orders):
        spline_func = cubic_spline(xd, yd)
        y_new = spline_func(x_new)
        axs[i].scatter(xd, yd, color='red', label='Data points')
        axs[i].plot(x_new, y_new, label= f"Cubic Spline")
        axs[i].set_title(f"{title} (Cubic Spline)", fontsize=12)
        axs[i].legend()

    plt.tight_layout()
    plt.savefig(output_file)
    print(f"Plot saved to {output_file}")

if __name__ == "__main__":

    base_dir = os.path.dirname(__file__)

    data_dir = os.path.join(base_dir, "data")
    '''    output_dir = os.path.join(base_dir, "figures")
    os.makedirs(output_dir, exist_ok=True)'''

    water_density_data = load_data(os.path.join(data_dir, "water_density_vs_temp_usgs.txt"))
    air_density_data = load_data(os.path.join(data_dir, "air_density_vs_temp_eng_toolbox.txt"))

    xd_water, yd_water = water_density_data[:, 0], water_density_data[:, 1]
    xd_air, yd_air = air_density_data[:, 0], air_density_data[:, 1]

    output_dir = os.path.join(base_dir, "figures")
    os.makedirs(output_dir, exist_ok=True)
    generate_spline_plot(xd_water, yd_water, "Water Density", os.path.join(output_dir, "water_density_splines.png"))
    generate_spline_plot(xd_air, yd_air, "Air Density", os.path.join(output_dir, "air_density_splines.png"))