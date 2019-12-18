#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os


# In[2]:


#Directory to traverse
Dir = "."


# In[26]:


files = list()
for dirName, subdirList, fileList in os.walk(Dir):
    print('Found directory: %s' % dirName)
    temp = list()
    for i in fileList:
        temp.append(os.path.join(dirName,i))
    files.extend(temp)


# In[27]:


files


# In[28]:


files2 = list()
for i in files:
    _,e = os.path.splitext(i)
    if e == '.png':
        files2.append(i)


# In[29]:


files2


# In[16]:


filewithp = list()
for i in files2:
    filewithp.append(os.path.join(Dir,i))


# In[17]:


filewithp


# In[ ]:




