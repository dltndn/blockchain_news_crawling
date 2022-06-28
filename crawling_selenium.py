from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import requests

class crawling_selenium:
    
    def crawling_with_selenium(self, url, index, xpath=0):  #return arr, arr
        title_arr = []
        href_arr = []
        URL = url
        
        if index == 0:  #bitcoinmagazine
            response = requests.get(URL)
            source = response.text
            html = BeautifulSoup(source, "html.parser")
            results = html.find_all("div", {"class": "l-grid--item"})
            for result in results:
              article_date = result.find("span" ,{"class": "mm-card--metadata-text"})
              if article_date is not None:
                article_date = str(result.find("span" ,{"class": "mm-card--metadata-text"}).string)
                if "hours" in article_date:
                  title = str(result.find("h2", {"class": "m-ellipsis--text m-card--header-text"}).string)
                  href = result.find("a")["href"]
                  href = url + href
                  title_arr.append(title)
                  href_arr.append(href)

            return title_arr, href_arr
                
        else:           #selenium
            driver = webdriver.Chrome()
            driver.implicitly_wait(100)
            driver.get(URL)
            source = driver.find_element(By.XPATH, xpath).get_attribute("innerHTML")
            html = BeautifulSoup(source, "html.parser")   
            if index == 1:  #coindesk
                results = html.find_all("div", {"class": "jjrrtf"})
                for result in results:
                  article_date = result.find("span", {"class": "cqrEJU"}).text
                  if "Today" in article_date or "ago" in article_date:
                      obj = result.find("a", {"class" : "gBreWF"})
                      title = obj["title"]
                      href = obj["href"]
                      href = url + href
                      title_arr.append(title)
                      href_arr.append(href)
              
                return title_arr, href_arr
              
            elif index == 2:  #cointelegraph
                results = html.find_all("article", {"class": "post-card__article"})
                for result in results:
                  article_date = result.find("time", {"class" : "post-card__date"}).text
                  if "hour" in article_date:
                      obj = result.find("a", {"class" : "post-card__title-link"})
                      title = obj["title"]
                      href = obj["href"]
                      href = url + href
                      title_arr.append(title)
                      href_arr.append(href)
              
                return title_arr, href_arr
              
            elif index == 3:  #bloomingbit
                results = html.find_all("a")
                for result in results:
                  title = result.find("h3").text
                  title = title.strip()
                  href = result["href"]
                  href = href.lstrip('/news')
                  href = url + href
                  title_arr.append(title)
                  href_arr.append(href)
              
                return title_arr, href_arr    
