#Driver script
import os
import numpy as np
import matplotlib.pyplot as plt
from src.linalg_interp import cubic_spline

def load_data(file_path):
    return np.loadtxt(file_path, delimiter=',')

def generate_spline_plot(xd, yd, title, output_file):
    fig, axs = plt.subplots(3, 2, figsize=(12, 12))
    orders = [1, 2, 3]
    x_new = np.linspace(xd[0], xd[-1], 100)
    axs = axs.ravel()

    for i, order in enumerate(orders):
        spline_func = cubic_spline(xd, yd, order=order)
        y_new = spline_func(x_new)
        axs[i].scatter(xd, yd, color='red', label='Data points')
        axs[i].plot(x_new, y_new, label= f'order {order}')
        axs[i].set_title(f"Spline Interpolation (order {order})")
        axs[i].legend()

    plt.tight_layout()
    plt.savefig(output_file)

if __name__ == "__main__": #type: ignore

    water_density_data = load_data("data/water_density_vs_temp_usgs.txt")
    air_density_data = load_data("data/air_density_vs_temp_eng_toolbox.txt")

    xd_water, yd_water = water_density_data[:, 0], water_density_data[:, 1]
    xd_air, yd_air = air_density_data[:, 0], air_density_data[:, 1]

    generate_spline_plot(xd_water, yd_water, "Water Density", "figures/water_density_splines.png")
    generate_spline_plot(xd_air, yd_air, "Air Density", "figures/air_density_splines.png")