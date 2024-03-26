#!/usr/bin/env python
# coding: utf-8

# In[1]:


from bs4 import BeautifulSoup
import requests


# In[2]:


url = 'https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue'

page = requests.get(url)

soup = BeautifulSoup(page.text, 'html')


# In[3]:


print(soup)


# In[4]:


soup.find_all('table')


# In[5]:


soup.find_all('table')[1]


# In[6]:


soup.find('table',class_ = 'wikitable sortable')


# In[7]:


table = soup.find_all('table')[1]


# In[8]:


print(table)


# In[14]:


world_titles = table.find_all('th')


# In[11]:


world_titles


# In[15]:


world_table_titles = [title.text.strip() for title in world_titles]

print(world_table_titles)


# In[16]:


import pandas as pd


# In[17]:


df = pd.DataFrame(columns = world_table_titles)

df


# In[19]:


column_data = table.find_all('tr')


# In[23]:


for row in column_data[1:]:
    row_data = row.find_all('td')
    individual_row_data = [data.text.strip() for data in row_data]
    
    length = len(df)
    df.loc[length] = individual_row_data
    
    


# In[24]:


df


# In[26]:


df.to_csv(r'D:\Python项目\Companies.csv',index = False)


# In[ ]:




