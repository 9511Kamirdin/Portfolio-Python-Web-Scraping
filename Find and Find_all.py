#!/usr/bin/env python
# coding: utf-8

# In[1]:


from bs4 import BeautifulSoup
import requests


# In[2]:


url = "https://www.scrapethissite.com/pages/forms/"


# In[3]:


page = requests.get(url)


# In[4]:


soup = BeautifulSoup(page.text, 'html')


# In[5]:


print(soup)


# In[6]:


soup.find('div')


# In[8]:


soup.find_all('div',class_ = 'col-md-12')


# In[9]:


soup.find_all('p',class_ = 'lead')


# In[10]:


soup.find('p',class_ = 'lead').text


# In[11]:


soup.find_all('th')


# In[12]:


soup.find_all('td')


# In[13]:


soup.find('th').text.strip()


# In[ ]:




