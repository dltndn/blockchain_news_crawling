import requests
from bs4 import BeautifulSoup
from time import localtime

class text_to_telegram:
      
  def get_current_date(self): 
    tm = localtime()
    current_date = tm.tm_mday
    return current_date
        
  def get_text(self, URL):
    self.URL = URL
    

    # get title from site 
    
    # loop several options

    

    element = '' # result

    # driver.close()
    return element

  def loop_option(self, xpath):
    self.xpath = xpath
    
  def crawling_bitcoinmagazine(self, date): #get_text()
    current_date = date
    URL = 'https://bitcoinmagazine.com/'
    response = requests.get(URL)
    html = response.text
    print(current_date)
    
    
  
    
  # def translation_e_to_k():
        
test = text_to_telegram()
test.crawling_bitcoinmagazine(test.get_current_date())