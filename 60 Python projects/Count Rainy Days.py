"""
Count Rainy Days.
Analyzes Seattle rainfall data from a CSV file and prints summary statistics.
"""

import os
import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def main():
    """Load rainfall data, compute statistics, and display a histogram."""
    csv_file = "Seattle2014.csv"

    # Check if the CSV file exists before trying to read it
    if not os.path.exists(csv_file):
        print(f"Error: '{csv_file}' not found in the current directory.")
        print("Please download Seattle2014.csv and place it alongside this script.")
        sys.exit(1)

    # Read rainfall data from CSV
    rainfall = pd.read_csv(csv_file)['PRCP'].values
    inches = rainfall / 254  # Convert tenths of mm to inches

    print(f"Data shape: {inches.shape}")

    # Plot histogram of rainfall distribution
    plt.hist(inches, bins=40)
    plt.title("Seattle Rainfall Distribution (2014)")
    plt.xlabel("Inches of rain")
    plt.ylabel("Frequency")
    # plt.show()

    # Calculate and display rainfall statistics
    days_no_rain = int(np.sum(inches == 0))
    days_with_rain = int(np.sum(inches != 0))
    days_heavy_rain = int(np.sum(inches > 0.5))
    days_light_rain = int(np.sum((inches > 0) & (inches < 0.2)))

    print(f"Number of days without rain: {days_no_rain}")
    print(f"Number of days with rain: {days_with_rain}")
    print(f"Days with more than 0.5 inches of rain: {days_heavy_rain}")
    print(f"Rainy days with < 0.1 inches: {days_light_rain}")
    print(f"Rainy days with < 0.2 inches: {days_light_rain}")


if __name__ == '__main__':
    main()
