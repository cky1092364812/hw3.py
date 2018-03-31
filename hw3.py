
# coding: utf-8

# In[ ]:


import collections

text = collections.Counter(input('Please type anything: '))
result = dict(text)
for key,val in result.items():
    print("'"+key+"':",val)

