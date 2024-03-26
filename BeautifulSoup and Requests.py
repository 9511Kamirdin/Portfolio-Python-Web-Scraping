#!/usr/bin/env python
# coding: utf-8

# In[2]:


from bs4 import BeautifulSoup
import requests


# In[3]:


url = "https://www.scrapethissite.com/pages/forms/"


# In[5]:


page = requests.get(url)


# In[8]:


soup = BeautifulSoup(page.text, 'html')


# In[11]:


print(soup.prettify())


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




