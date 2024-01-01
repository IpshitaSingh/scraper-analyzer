import scraper
import analyzer

def main():
    url = 'https://www.scrapethissite.com/pages/simple/'
    df = scraper.create_df(url)
    result = data_analysis(df)
    print("Analysis Result:", result)

def data_analysis(df):
    return analyzer.check_missing_values(df), analyzer.explore_data(df), analyzer.visualize_data(df)

if __name__ == "__main__":
    main()



