import requests
from bs4 import BeautifulSoup


def simple_scraper(terms):
    url = f'https://www.ptt.cc/bbs/Gossiping/search?q={terms}'
    response = requests.get(url)
    response.raise_for_status()  

    soup = BeautifulSoup(response.content, 'html.parser')

    title = soup.select_one('div.r-ent > div.title > a').text

    return title
  
