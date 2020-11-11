#!/usr/bin/env python
# coding: utf-8

# In[2]:


get_ipython().system('pip install selenium')
get_ipython().system('pip install unidecode')


# In[10]:


from bs4 import BeautifulSoup
from selenium import webdriver
from unidecode import unidecode
import pandas


# In[11]:


from bs4 import BeautifulSoup
from selenium import webdriver
from unidecode import unidecode
import pandas



class stock():
    Name = ''
    Url = ''
    Buy = ''
    Sell = ''
    Neutral = ''


url = 'https://rahavard365.com/stock'
base = 'https://rahavard365.com'

driver = webdriver.Chrome(executable_path=r'C:\Users\ASUS\Downloads\Compressed\chromedriver')
driver.get(url)
htmlSource = driver.page_source
df = pandas.DataFrame(columns=["Name", "Buy", "Neutral", "Sell"])

try:
    soup = BeautifulSoup(htmlSource, "html.parser")
    for i in soup.findAll('a', {'class': 'symbol'}):                             ### <a class="symbol">
        item = stock
        item.Name = i.text
        item.Url = base + i['href']
        driver.get(item.Url)
        htmlSource = driver.page_source
        soup = BeautifulSoup(htmlSource, "html.parser")
        item.Buy = unidecode(soup.find('div', {'id': 'indc_buy'}).text)           ### <div id="indc_buy">
        item.Sell = unidecode(soup.find('div', {'id': 'indc_sell'}).text)         ### <div id="indc_sell">
        item.Neutral = unidecode(soup.find('div', {'id': 'indc_neutral'}).text)   ### <div id="indc_neutral"> 
        df.loc[len(df)] = [item.Name, item.Buy, item.Neutral, item.Sell]
    driver.quit()
except:
    pass

df.to_csv("data.csv", sep=',', index=False)




