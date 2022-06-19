import requests
from bs4 import BeautifulSoup
from time import localtime

class text_to_telegram:
      
  def get_current_date(self): 
    tm = localtime()
    current_date = tm.tm_mday
    return current_date
    
  def crawling_bitcoinmagazine(self, date): #get_information()
    title_arr = []
    href_arr = []
    current_date = date
    URL = 'https://bitcoinmagazine.com/'
    response = requests.get(URL)
    html = BeautifulSoup(response.text, "html.parser")          
    
    results = html.find_all("div", {"class": "l-grid--item"})
    for result in results:
      article_date = result.find("span" ,{"class": "mm-card--metadata-text"})
      if article_date is not None:
        article_date = str(result.find("span" ,{"class": "mm-card--metadata-text"}).string)
        if "hours" in article_date:
          title = str(result.find("h2", {"class": "m-ellipsis--text m-card--header-text"}).string)
          href = result.find("a")["href"]
          title_arr.append(title)
          href_arr.append(href)
    
    return title_arr, href_arr  #arr type
    
  def crawling_cointelegraph(self, date):
    title_arr = []
    article_date_arr = []
    href_arr = []
    current_date = date
    URL = 'https://cointelegraph.com/'
    response = requests.get(URL)
    html = BeautifulSoup(response.text, "html.parser")   
    print(html)
    
  # def translation_e_to_k():
  
  def crawling_bloomingbit(self, date):
    title_arr = []
    article_date_arr = []
    href_arr = []
    current_date = date
    URL = 'https://bloomingbit.io/news'
    response = requests.get(URL)
    html = BeautifulSoup(response.text, "html.parser")   
    print(html)
        
test = text_to_telegram()
test.crawling_bloomingbit(test.get_current_date())