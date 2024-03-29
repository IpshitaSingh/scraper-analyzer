"""
Main Module

This module ties together both the Scraper and Analyzer modules & uses their functions to
provide the plots and data stats all at once.

Dependencies:
    - scraper.py
    - analyzer.py

Functions:
    - main()
        Uses the dataframe generated by Scraper to print the analysis and visualization
        of data.
        - Provides info related to dataframe shape (no. of rows & columns), data types,
        & summary statistics.
        - Provides plots related to Top 20 countries by Population, Population Distribution,
        Area v/s Population, & Variable Correlation.
    - data_analysis(df)
        Uses functions from Analyzer to create analysis & visualization of data.
"""

import scraper
import analyzer

df = scraper.data_frame

def main():
    """Uses the dataframe generated by Scraper to print data stats & plots"""
    result = data_analysis(df)
    print("Analysis Result:", result)

def data_analysis(df):
    """Uses functions from Analyzer to create analysis & visualization of df"""
    return analyzer.check_missing_values(df), analyzer.explore_data(df), analyzer.visualize_data(df)

if __name__ == "__main__":
    main()
