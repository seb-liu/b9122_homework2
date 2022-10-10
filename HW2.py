#!/usr/bin/env python
# coding: utf-8

# In[5]:


from bs4 import BeautifulSoup
import requests
import re
import urllib.request
from tqdm import tqdm


# In[6]:


#1.1
seed_url = "https://www.federalreserve.gov/newsevents/pressreleases.htm"

urls = [seed_url]    
seen = [seed_url]    
opened = []

def collect(curr_url):
    while len(urls) > 0:
        try:
           
            #print("num. of URLs in stack: %d " % len(urls))
            #print("Trying to access= "+curr_url)
            req = urllib.request.Request(curr_url,headers={'User-Agent': 'Mozilla/5.0'})
            webpage = urllib.request.urlopen(req).read()
            opened.append(curr_url)

        except Exception as ex:
            print("Unable to access= "+curr_url)
            print(ex)
            continue

        soup = BeautifulSoup(webpage)  #creates object soup
        url_result = []

        for tag in soup.find_all('a', href = True): #find tags with links
            url_result.append(str(tag.get('href')).strip())
        return url_result


# In[7]:


website = 'https://www.federalreserve.gov/newsevents/pressreleases.htm'
keyword = 'covid'
a = collect(website)
text = '/'
tail = [idx for idx in a if idx[0].lower() == text.lower()]
url_head = 'https://www.federalreserve.gov'
result=[]
for url_tail in tqdm(tail):
    url = url_head + url_tail
    html = requests.get(url)
    soup = BeautifulSoup(html.text)
    text = soup.get_text()
    text = text.lower()
    if keyword in text:
        result.append(url)
    if len(result) == 10:
        break
print(result)


# In[8]:


#1.2
website = 'https://www.sec.gov/news/pressreleases'
keyword = 'charge'
b = collect(website)
text = '/'
restrict = '/news/press-release/'
c = []
for url in b:
    if len(url) != 0:
        c.append(url)
tail = [idx for idx in c if restrict in idx]

url_head = 'https://www.sec.gov'
sol = []
for url_tail in tqdm(tail):
    url = url_head + url_tail
    html = requests.get(url)
    soup = BeautifulSoup(html.text)
    text = soup.get_text()
    text = text.lower()
    if keyword in text:
        sol.append(url)
    if len(sol) == 20:
        break
print(sol)


# In[9]:


sol_text=[]
for a in sol:
    text_final = []
    website = requests.get(a)
    text = BeautifulSoup(website.text).get_text()
    text_final.append(a)
    text_final.append(text)
    sol_text.append(text_final)
for i in sol_text:
    print(i)


# In[ ]:




