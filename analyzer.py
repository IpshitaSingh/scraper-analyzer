#import scraper
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#renaming imported df
#df = scraper.data_frame

#data exploration
def check_missing_values(df):
    #checking for missing values 
    #True if there are missing values, False otherwise
    missing_values = df.isnull().sum().sum()
    if missing_values > 0:
        print(f"There are {missing_values} missing values in the DataFrame.")
        return True
    else:
        print("No missing values found in the DataFrame.")
        return False

#data summary 
def explore_data(df):
    #setting display options to avoid scientific notation
    pd.set_option('display.float_format', lambda x: '%.2f' % x) 
    rows, cols = df.shape
    data_types = df.dtypes 
    summary_stats = df.describe()
    print(f"\nDataFrame Shape: {rows} rows x {cols} columns")
    print("\nData Types:")
    print(data_types)
    print("\nSummary Statistics:")
    print(summary_stats)

#data analysis & visualization
def visualize_data(df):
    sns.set(style="whitegrid")

    #Plot 1: Top 20 Countries by population
    plt.figure(figsize=(8, 6))
    top_countries = df.sort_values(by='Population', ascending=False).head(20)
    sns.barplot(x='Population', y='Country', data=top_countries, palette='crest')
    plt.title('Top 20 Countries by Population')
    plt.xlabel('Population')
    plt.ylabel('Country')
    plt.show()

    # Plot 2: Population distribution 
    plt.figure(figsize=(8, 6))
    #defining bin edges using powers of 10 (was in decimal pt before)
    bin_edges = [10 ** i for i in range(5, 8)]
    sns.histplot(df['Population'], bins=bin_edges, kde=True, color='seagreen')
    plt.xscale('log')  #logarithmic scale for the x-axis
    plt.title('Population Distribution')
    plt.xlabel('Population (log scale)')
    plt.ylabel('Frequency')
    plt.show()

   # Plot 3: Area vs. Population 
    plt.figure(figsize=(8, 6))
    sns.scatterplot(x='Area', y='Population', data=df, color='seagreen')
    plt.xscale('log')  # Logarithmic scale for the x axis for better visibility of data pts
    plt.title('Area vs. Population')
    plt.xlabel('Area (sq km)')
    plt.ylabel('Population')
    plt.show()
       
    # Plot 4: Scatter Plots to depict correlation b/w variables
    plt.figure(figsize=(8, 6))
    scatter_kws = {'s': 100, 'alpha': 0.7, 'color':'seagreen'}
    diag_kws = {'bins': 20,'edgecolor': 'k'}
    sns.pairplot(df[['Population', 'Area']], height=3, aspect=1.2,
                 kind='scatter', diag_kind='hist', markers='o',
                 plot_kws=scatter_kws, diag_kws=diag_kws)
    plt.suptitle('Scatter Plots', y=1.02)
    plt.xlim(0, 2100000)
    plt.ylim(0, 11000)
    plt.show()
    
# def data_analysis():
#     return check_missing_values(df), explore_data(df), visualize_data(df)




