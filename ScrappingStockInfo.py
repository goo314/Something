from urllib.parse import quote
import requests
from bs4 import BeautifulSoup

def findPrice(stock):
    url = "https://www.google.com/search?q="+stock+"+stock"
    html_source = requests.get(url)
    plain_text = html_source.text
    soup = BeautifulSoup(plain_text, 'html.parser')

    a = soup.find('body')
    b = a.find_all('div')
    c = b[7].find('div', {'class':'BNeawe iBp4i AP7Wnd'})
    d = (c.text).split()[0]
    price = float(d.replace(',', ''))
    return price
# //*[@id="knowledge-finance-wholepage__entity-summary"]
# /div/g-card-section/div/g-card-section/div[2]/div[1]/span[1]/span/span[2]

# //*[@id="knowledge-finance-wholepage__entity-summary"]
# /div/g-card-section/div/g-card-section/div[2]/div[1]/span[1]/span/span[1]
s = input('What company are you looking for : ')
print('Current price is', findPrice(s))
