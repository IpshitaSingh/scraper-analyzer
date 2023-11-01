from scraper import scrape_data
from analyzer import analyze_data

def main():
    url = "..."  #to be added later
    scraped_data = scrape_data(url)
    if scraped_data:
        analyzed_result = analyze_data(scraped_data)

        print("Analysis Result:", analyzed_result)

if __name__ == "__main__":
    main()

