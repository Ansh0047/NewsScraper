import requests
from bs4 import BeautifulSoup
import pandas as pd

def bbcNews():
    url = 'https://www.bbc.com/news'
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        headlines = []

        for item in soup.find_all('h2', class_='sc-4fedabc7-3'):
            link_tag = item.find_parent('a')  
            if link_tag:
                title = item.text.strip()
                link = link_tag['href']
                
                if not link.startswith('http'):
                    link = f'https://www.bbc.com{link}'
                headlines.append({"source": "BBC News", 'title': title, 'link': link})

        return headlines
    else:
        print(f"Failed to retrieve content: {response.status_code}")
        return []
    
    
def fitnessNews():
    url = 'https://breakingmuscle.com/'
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        
        articles = []
        for item in soup.find_all('h2',class_= "wp-block-post-title"):
            title = item.text.strip()
                    
            link = item.find('a')['href']
            articles.append({"source": "Fitness", 'title': title, 'link': link,})
        return articles
    else:
        print(f"Failed to retrieve content: {response.status_code}")
        return []


def sportsNews():
    url = 'https://indianexpress.com/section/sports/'
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        
        articles = []
        for item in soup.find_all('h2', class_="title"):
            title = item.text
            link = item.find('a')['href']
            articles.append({"source": "Sports", 'title': title, 'link': link})
        return articles
    else:
        print(f"Failed to retrieve content: {response.status_code}")
        return []
    

def timesOfIndia():
    url = 'https://timesofindia.indiatimes.com/'
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        
        articles = []
        for item in soup.find_all('figure', class_='_YVis'):
            title = item.find('figcaption').text
            link = item.find('a')['href']
            articles.append({"source": "Times of India", 'title': title, 'link': link})
        return articles
    else:
        print(f"Failed to retrieve content: {response.status_code}")
        return []
    

def techNews():
    url = 'https://www.gadgets360.com/news'
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        
        articles = []
        for item in soup.find_all('div', class_="caption_box"):
            title = item.find('span').text
            link = item.find('a')['href']
            articles.append({"source": "Tech",'title': title, 'link': link})
        return articles
    else:
        print(f"Failed to retrieve content: {response.status_code}")
        return []

def save_data():
    data = bbcNews() + timesOfIndia() + fitnessNews() + techNews() + sportsNews()
    df = pd.DataFrame(data)
    df.to_csv('scraped_news.csv', index=False) # save the DataFrame to a CSV file
        