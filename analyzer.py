"""
Analysis Module

This module uses functions for data exploration of generated dataframe and performs
analysis and visualization on it.

Dependencies:
    - pandas
    - pyplot from matplotlib
    - seaborn

Functions:
    - check_missing_values(data_frame)
        Checks for missing data from the df. Returns a statment accordingly.
    - explore_data(data_frame)
        Exolores and summarizes the data.
        Provides info regarding dataframe shape (no. of rows & columns), data types,
        & summary statistics.
    - visualize_data(data_frame)
        Visualizes the data based on its analysis.
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#renaming imported dataFrame
#data_frame = scraper.data_frame

#data exploration
def check_missing_values(data_frame):
    """checking for missing values"""
    #True if there are missing values
    missing_values = data_frame.isnull().sum().sum()
    if missing_values > 0:
        print(f"There are {missing_values} missing values in the DataFrame.")
        return True
    #False if there are no missing values
    print("No missing values found in the DataFrame.")
    return False

#data summary
def explore_data(data_frame):
    """setting display options to avoid scientific notation"""
    pd.set_option('display.float_format', lambda x: f'{x:.2f}')
    rows, cols = data_frame.shape
    data_types = data_frame.dtypes
    summary_stats = data_frame.describe()
    print(f"\nDataFrame Shape: {rows} rows x {cols} columns")
    print("\nData Types:")
    print(data_types)
    print("\nSummary Statistics:")
    print(summary_stats)

#data analysis & visualization
def visualize_data(data_frame):
    """creating plots"""
    sns.set(style="whitegrid")

    #Plot 1: Top 20 Countries by population
    plt.figure(figsize=(8, 6))
    top_countries = data_frame.sort_values(by='Population', ascending=False).head(20)
    sns.barplot(x='Population', y='Country', data=top_countries, palette='crest')
    plt.title('Top 20 Countries by Population')
    plt.xlabel('Population')
    plt.ylabel('Country')
    plt.show()

    # Plot 2: Population distribution
    plt.figure(figsize=(8, 6))
    #defining bin edges using powers of 10 (was in decimal pt before)
    bin_edges = [10 ** i for i in range(5, 8)]
    sns.histplot(data_frame['Population'], bins=bin_edges, kde=True, color='seagreen')
    plt.xscale('log')  #logarithmic scale for the x-axis
    plt.title('Population Distribution')
    plt.xlabel('Population (log scale)')
    plt.ylabel('Frequency')
    plt.show()

   # Plot 3: Area vs. Population
    plt.figure(figsize=(8, 6))
    sns.scatterplot(x='Area', y='Population', data=data_frame, color='seagreen')
    plt.xscale('log')  # Logarithmic scale for the x axis for better visibility of data pts
    plt.title('Area vs. Population')
    plt.xlabel('Area (sq km)')
    plt.ylabel('Population')
    plt.show()

    # Plot 4: Scatter Plots to depict correlation b/w variables
    plt.figure(figsize=(8, 6))
    scatter_kws = {'s': 100, 'alpha': 0.7, 'color':'seagreen'}
    diag_kws = {'bins': 20,'edgecolor': 'k'}
    sns.pairplot(data_frame[['Population', 'Area']], height=3, aspect=1.2,
                 kind='scatter', diag_kind='hist', markers='o',
                 plot_kws=scatter_kws, diag_kws=diag_kws)
    plt.suptitle('Scatter Plots to depict Variable Correlation', y=1.02)
    plt.xlim(0, 2100000)
    plt.ylim(0, 11000)
    plt.show()