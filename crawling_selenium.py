from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import localtime
from bs4 import BeautifulSoup
import requests

class crawling_selenium:
    
    def get_current_date(self): 
        tm = localtime()
        current_date = tm.tm_mday
        return current_date
    
    def crawling_coindesk(self, date):
        title_arr = []
        href_arr = []
        current_date = date
        URL = "https://www.coindesk.com/"
        driver = webdriver.Chrome()
        driver.get(URL)
        xpath = '//*[@id="fusion-app"]/div/div[2]/div/main/div[2]/section[1]/div/div[2]/div/div[1]/div/div/div[2]'
        news_box = driver.find_element(By.XPATH, xpath).get_attribute("innerHTML")
        html = BeautifulSoup(news_box, "html.parser")
        results = html.find_all("div", {"class": "jjrrtf"})
        
        for result in results:
            article_date = result.find("span", {"class": "cqrEJU"}).text
            if "Today" in article_date or "ago" in article_date:
                obj = result.find("a", {"class" : "gBreWF"})
                title = obj["title"]
                href = obj["href"]
                title_arr.append(title)
                href_arr.append(href)
        
        return title_arr, href_arr
    
    def crawling_cointelegraph(self, date):
        title_arr = []
        href_arr = []
        current_date = date
        URL = "https://cointelegraph.com/"
        driver = webdriver.Chrome()
        driver.get(URL)
        xpath = '//*[@id="__layout"]/div/div[1]/main/div/div/div[2]/div/ul'
        news_box = driver.find_element(By.XPATH, xpath).get_attribute("innerHTML")
        html = BeautifulSoup(news_box, "html.parser")
        results = html.find_all("article", {"class": "post-card__article"})
        
        for result in results:
            article_date = result.find("time", {"class" : "post-card__date"}).text
            if "hour" in article_date:
                obj = result.find("a", {"class" : "post-card__title-link"})
                title = obj["title"]
                href = obj["href"]
                title_arr.append(title)
                href_arr.append(href)
        
        return title_arr, href_arr
    
    def crawling_bloomingbit(self, date):
        title_arr = []
        href_arr = []
        current_date = date
        URL = 'https://bloomingbit.io/news'
        driver = webdriver.Chrome()
        driver.get(URL)
        xpath = '//*[@id="__layout"]/div/div[1]/div/section[2]/section[2]'
        news_box = driver.find_element(By.XPATH, xpath).get_attribute("innerHTML")
        html = BeautifulSoup(news_box, "html.parser")
        results = html.find_all("a")
        
        for result in results:
            title = result.find("h3").text
            title = title.lstrip()
            href = result["href"]
            title_arr.append(title)
            href_arr.append(href)
        
        return title_arr, href_arr
    
    def crawling_with_selenium(self, url, index=0, xpath=0):
        title_arr = []
        href_arr = []
        URL = url
        
        if index == 0:  #selenium none
            response = requests.get(URL)
            source = response.text
            html = BeautifulSoup(source, "html.parser")
            results = html.find_all("div", {"class": "l-grid--item"})
            
        else:           #selenium
            driver = webdriver.Chrome()
            driver.get(URL)
            xpath = xpath
            source = driver.find_element(By.XPATH, xpath).get_attribute("innerHTML")
            html = BeautifulSoup(source, "html.parser")   
            if index == 1:
                results = html.find_all("div", {"class": "jjrrtf"})
            elif index == 2:
                results = html.find_all("article", {"class": "post-card__article"})
            elif index == 3:
                results = html.find_all("a")        
        
test = crawling_selenium()
test.crawling_coindesk(test.get_current_date())