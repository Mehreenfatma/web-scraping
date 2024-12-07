import warnings
warnings.filterwarnings("ignore", message="Pyarrow will become a required dependency of pandas")

import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_website(url):
    # Send HTTP request
    response = requests.get(url)
    if response.status_code != 200:
        print("Failed to retrieve the webpage")
        return None
    
    # Parse the HTML content
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Extract required data (example: titles and links)
    data = []
    for item in soup.find_all('div', class_='content-class'):  # Modify as per the site's structure
        title = item.find('h2').text.strip()
        link = item.find('a')['href']
        data.append({'Title': title, 'Link': link})
    
    return data