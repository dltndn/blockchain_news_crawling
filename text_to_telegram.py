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
    article_date_arr = []
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
          article_date_arr.append(article_date)
          href_arr.append(href)
    
    return title_arr, article_date_arr, href_arr #arr type
    
  def crawling_coindesk(self, date):
    title_arr = []
    article_date_arr = []
    href_arr = []
    current_date = date
    URL = "https://www.coindesk.com/"
    response = requests.get(URL)
    html = BeautifulSoup(response.text, "html.parser")   
    
    results = html.find_all("svg", {"class" : "desktop-navigationstyles__StyledLogo-sc-1dlegy5-10 kaptNW scroll-up"})
    print(results)
    for result in results:
      article_date = result.find("div", {"class" : "live-wirestyles__Time-sc-1xrlfqv-0 dfBMaW"})
      print(article_date)
     
    
  # def translation_e_to_k():
        
test = text_to_telegram()
test.crawling_coindesk(test.get_current_date())