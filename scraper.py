import requests
from bs4 import BeautifulSoup

url = '...' #to be chosen later

def scrape_data(url):
    page = requests.get(url)
    
    if page.status_code == 200:
        soup = BeautifulSoup(page.content, 'html.parser')
        # Extract relevant data from the HTML using BeautifulSoup
        data = ...  
        return data
    else:
        print("Failed to retrieve data. Status code:", page.status_code)
        return None


