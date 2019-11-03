#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import matplotlib.pyplot as plt
df= pd.read_csv('C:/Users/Danny Chacko/Downloads/DTMlemma.csv')
def s(word):
    return word.strip()
df['Date']= pd.to_datetime(df['Date'].apply(s)) #set all dates to datetime object


# In[ ]:


from datetime import datetime as dt
a= df.sort_values(by='Date')#sorting datetime object by date
a['Date'] = a['Date'].dt.strftime("%m") + a['Date'].dt.strftime("%Y")#isolates month and year before combining them


# In[ ]:


#For Trump
import matplotlib.pyplot as plt
trump_dict={}
Trump_full = a[a['Name'] == 'Donald Trump']
t_police = Trump_full.filter(['police','Date'])
t_months = t_police['Date'].unique().tolist()
for month in t_months:
    month_police= t_police[t_police['Date'] == month].sum(axis=0)
    trump_dict[month]= float(month_police.drop('Date'))
print(trump_dict)

plt.title("Trump's words")
plt.bar(range(len(trump_dict)), list(trump_dict.values()), align='center')
plt.xticks(range(len(trump_dict)), list(trump_dict.keys())) #X-label now is words


# In[ ]:


#For Theresa
import matplotlib.pyplot as plt
import numpy as np
theresa_dict={}
Theresa_full = a[a['Name'] == 'Theresa May']
m_police = Theresa_full.filter(['police','Date'])
m_months = m_police['Date'].unique().tolist()
for month in t_months:
    month_police= m_police[m_police['Date'] == month].sum(axis=0)
    theresa_dict[month]= float(month_police.drop('Date'))
print(theresa_dict)

plt.title("Theresa's words")
plt.bar(range(len(theresa_dict)), list(theresa_dict.values()), align='center')
plt.xticks(range(len(theresa_dict)), list(theresa_dict.keys())) #X-label now is words


# In[ ]:


#For Scott
scott_dict={}
Scott_full = a[a['Name'] == 'Scott Morrison']
Sc_police = Scott_full.filter(['police','Date'])
Sc_months = Sc_police['Date'].unique().tolist()
for month in Sc_months:
    month_police= Sc_police[Sc_police['Date'] == month].sum(axis=0)
    scott_dict[month]= float(month_police.drop('Date'))
print(scott_dict)

plt.title("Scott's words")
plt.bar(range(len(scott_dict)), list(scott_dict.values()), align='center')
plt.xticks(range(len(scott_dict)), list(scott_dict.keys())) #X-label now is words


# In[ ]:


#Correlation overall
get_ipython().run_line_magic('matplotlib', 'notebook')
from scipy.stats import spearmanr
#plt.plot(list(theresa_dict.values()), list(trump_dict.values()))
def compare_2_dicts(dict_1, dict_2, person1, person2, word):
    keyword= []
    nums=[]
    dict1= dict_1.copy()
    dict2= dict_2.copy()
    for key in dict1:
        if key not in dict2:
            dict2[key]= float(0)
    for key in dict2:
        if key not in dict1:
            dict1[key]= float(0)  
        for num in key:
            nums.append(num)
        keyword.append(nums[-4]+nums[-3]+nums[-2]+nums[-1])

    keyword= set(keyword)
    for year in keyword:
        plot_dict1=[]
        plot_dict2=[]
        for key in dict1:
            if "122" not in key and dict1[key] != 0:
                
                key1= str(int(key)+10000)
                if len(key1) < 6:
                    key1= "0" + key1
                if key1 not in dict2:
                    pass
                else:
                    if dict2[key1] == 0:
                        dict1[key1] += dict1[key] #If no value of Trump, add frequency of police to next month for effect
                    else:
                        plot_dict2.append(dict2[key1])
                        plot_dict1.append(dict1[key])

        plt.scatter(plot_dict1, plot_dict2)
        plt.title(word)
        plt.xlabel(person1)
        plt.ylabel(person2)
        return plot_dict1, plot_dict2

list1, list2= compare_2_dicts(theresa_dict, trump_dict, "Theresa May", "Donald Trump", "police")
list3, list4= compare_2_dicts(theresa_dict, scott_dict, "Theresa May", "Scott Morrison", "police")
list5, list6= compare_2_dicts(trump_dict, scott_dict, "Donald Trump", "Scott Morrison", "police")
print(spearmanr(list1, list2))
print(spearmanr(list3, list4))
print(spearmanr(list5, list6))


# In[ ]:


trump_china_dict={}
Trump_full = a[a['Name'] == 'Donald Trump']
t_china = Trump_full.filter(['china','Date'])
t_months = t_china['Date'].unique().tolist()
#t_police[t_police['Date'] == t_months[0]]
for month in t_months:
    month_china= t_china[t_china['Date'] == month].sum(axis=0)
    trump_china_dict[month]= float(month_china.drop('Date'))
print(trump_china_dict)

plt.title("Trump's word- China")
plt.bar(range(len(trump_china_dict)), list(trump_china_dict.values()), align='center')
plt.xticks(range(len(trump_china_dict)), list(trump_china_dict.keys())) #X-label now is words


# In[ ]:


theresa_china_dict={}
Theresa_full = a[a['Name'] == 'Theresa May']
m_china = Theresa_full.filter(['china','Date'])
m_months = m_china['Date'].unique().tolist()
for month in t_months:
    month_china = m_china[m_china['Date'] == month].sum(axis=0)
    theresa_china_dict[month]= float(month_china.drop('Date'))
print(theresa_china_dict)

plt.title("Theresa's words")
plt.bar(range(len(theresa_china_dict)), list(theresa_china_dict.values()), align='center')
plt.xticks(range(len(theresa_china_dict)), list(theresa_china_dict.keys())) #X-label now is words


# In[ ]:


#For Scott
scott_china_dict={}
Scott_full = a[a['Name'] == 'Scott Morrison']
Sc_china = Scott_full.filter(['china','Date'])
Sc_months = Sc_china['Date'].unique().tolist()
for month in Sc_months:
    month_china = Sc_china[Sc_china['Date'] == month].sum(axis=0)
    scott_china_dict[month]= float(month_china.drop('Date'))
print(scott_china_dict)

plt.title("Scott's words")
plt.bar(range(len(scott_china_dict)), list(scott_china_dict.values()), align='center')
plt.xticks(range(len(scott_china_dict)), list(scott_china_dict.keys())) #X-label now is words


# In[ ]:


get_ipython().run_line_magic('matplotlib', 'notebook')
from scipy.stats import spearmanr
#plt.plot(list(theresa_dict.values()), list(trump_dict.values()))

china_list1, china_list2= compare_2_dicts(theresa_china_dict, trump_china_dict, "Theresa May", "Donald Trump", "china")
china_list3, china_list4= compare_2_dicts(theresa_china_dict, scott_china_dict, "Theresa May", "Scott Morrison", "china")
china_list5, china_list6= compare_2_dicts(trump_china_dict, scott_china_dict, "Donald Trump", "Scott Morrison", "china")
print(spearmanr(china_list1, china_list2))
print(spearmanr(china_list3, china_list4))
print(spearmanr(china_list5, china_list6))

