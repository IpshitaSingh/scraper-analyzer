import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://www.scrapethissite.com/pages/simple/'

def get_soup(url):
    #send request to the specified URL
    response = requests.get(url)
    
    #checking if the request was successful 
    if response.status_code == 200:
        #extract the HTML content of the page
        soup = BeautifulSoup(response.content, 'html.parser')
        return soup
    else:
        print(f"Failed to retrieve data. Status Code: {response.status_code}")
        return None

def extract_country_data(country_element):
    try:
        #extract relevant data & return as dictionary (country name, capital, population, area)
        country_name = country_element.find('h3', class_ ="country-name").text.strip()
        capital = country_element.find('span', class_ = "country-capital").text.strip()
        population = int(country_element.find('span', class_ ="country-population").text.strip().replace(',', ''))
        area = float(country_element.find('span', class_ ="country-area").text.strip().replace(',', ''))

        return {
            'Country': country_name,
            'Capital': capital,
            'Population': population,
            'Area': area
        }
    except Exception as e:
        print(f"Error while extracting data: {e}")
        return None

def create_df(url):
    #scrape data from the website and create a dataframe
    soup = get_soup(url)
    
    if soup:
        #find the HTML elements containing country data
        country_elements = soup.find_all('div', class_='country')
        
        #extract data from each country element
        data_list = [extract_country_data(country_element) for country_element in country_elements if country_element]

        #create the df from the list of dictionaries
        df = pd.DataFrame(data_list)
        return df
    else:
        return None

# data_frame = create_df(url)

#print the DF if it's not empty
# if data_frame is not None:
#     print(data_frame)

