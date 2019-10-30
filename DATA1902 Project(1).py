#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
df= pd.read_csv('C:/Users/Danny Chacko/Downloads/test1.csv')
def s(word):
    return word.strip()
df['Date']= df['Date'].apply(s)


# In[3]:


get_ipython().run_line_magic('matplotlib', 'notebook')
sums= df.sum(axis=0)
#To get columns with letter A or a in name, just do df.filter(regex= '[aA]'), same for no.s
#Automate column dropping is string late
sums_filter= sums.drop(['Date', 'Title', 'Name'])
#sums= sums.reset_index
# Looking at data overall
sums_filter= sums_filter.astype('int64') #convert from object to int64 type
total= sums_filter.sum(axis=0)
print("There are a total of", total, "values in our dataset, with", df.shape[0], "rows and", df.shape[1], "columns.")

word= sums_filter.filter(regex= '^[A-Za-z]+$', axis=0)
print("The most used word is", "'" + word.idxmax() +"'.")

number= sums_filter.filter(regex= '[0-9]', axis=0)
print("The most used number is", number.idxmax() + ".")

sums_filter= sums_filter.sort_values(ascending= False)
top_100= sums_filter[:100]/total
import matplotlib.pyplot as plt
plt.title('Most 100 frequent words')
frame_1= top_100.plot(kind="bar")
frame_1.axes.xaxis.set_ticklabels([])


# In[5]:


top_25= sums_filter[:25]/total
plt.title('Top 25 words overall')
top_25.plot(kind="bar")


# In[6]:


min(sums_filter)


# In[7]:


def filter_by_name(names):
    name = df['Name'] == str(names)
    name_data = df[name]
    name_sum = name_data.sum(axis=0)
    name_sum = name_sum.drop(['Date', 'Title', 'Name'])
    name_sum = name_sum.astype('int64') #convert from object to int64 type
    name_sum = name_sum.sort_values(ascending= False)
    total= name_sum.sum(axis=0)
    top25= name_sum[:25]/total

    fig = plt.figure(figsize=plt.figaspect(1.))
    #ax= fig.add_subplot(2, 2, h)
    top25.plot(kind="bar")
    plt.title(names + "'s top 25 words")
        
        
def name_summary(names):
    name = df['Name'] == names
    name_data = df[name]
    name_sum = name_data.sum(axis=0)
    name_sum = name_sum.drop(['Date', 'Title', 'Name'])
    name_sum = name_sum.astype('int64')
    name_sum= name_sum[name_sum != 0] # To remove rows that have 0 in it

    #Getting total no.
    total= name_sum.sum(axis=0)   
    distinct= name_sum.count()
    print("There are a total of", total, "values and", distinct, "distinct values for", name_data.shape[0], "speeches by", names + ".")

    #Distinct words
    words= name_sum.filter(regex= '^[A-Za-z]+$', axis=0)
    words_distinct= words.count()
    print(names + " had used", words_distinct, "distinct words altogether.")

    print("Most common word for " + str(i) + " is" + " '" + name_sum.idxmax() + "'" + ", occuring", name_sum.max(), "times.")

    #Getting median frequency of word
    median= name_sum.median()
    print("The median frequency of words for " + names + " is " + str(median))

    #Getting mean frequency of word
    mean= int(name_sum.mean())
    print("The mean frequency of words for " + names + " is " + str(mean))
    print() 
    
names= df['Name'].unique().tolist()
for i in names:
    name_summary(i)
    filter_by_name(i)


# In[18]:


get_ipython().run_line_magic('matplotlib', 'notebook')
date_frame= df.copy()
date= date_frame['Date'].str.split(" ",n = 2, expand = True)#n controls how many splits I'm having, expand expands the splits to separate columns
date_frame['Date']= date[2]
year= date[2].unique().tolist()

h= []
for i in year:
    if isinstance(i, str) == False:
        h.append(i)
    elif i.isnumeric() == False:
        h.append(i)

for i in h:
    year.remove(i) #doing it this way, otherwise if I just did remove above, all won't be removed, as some will be skipped over 
    
def yearly_plot(year):
    years = date_frame['Date'] == year
    year_plot= date_frame[years]
    year_sum = year_plot.sum(axis=0)
    year_sum = year_sum.drop(['Date', 'Title', 'Name'])
    year_sum = year_sum.astype('int64') #convert from object to int64 type
    print("Most common word for " + year + " is" + " '" + year_sum.idxmax() + "'" + ", occuring", year_sum.max(), "times.")
    year_sum = year_sum.sort_values(ascending= False)
    top25= year_sum[:25]
        
    fig = plt.figure(figsize=plt.figaspect(1.))
    #ax= fig.add_subplot(2, 2, h)
    top25.plot(kind="bar")
    plt.title(year)
    
def yearly_summary(year):
    years = date_frame['Date'] == year
    year_plot= date_frame[years]
    year_sum = year_plot.sum(axis=0)
    year_sum = year_sum.drop(['Date', 'Title', 'Name'])
    year_sum = year_sum.astype('int64')
    year_sum= year_sum[year_sum != 0] # To remove rows that have 0 in it
    
    #Getting total no.
    total= year_sum.sum(axis=0)   
    distinct= year_sum.count()
    print("There are a total of", total, "values and", distinct, "distinct values in", year + ".")
    
    #Getting median frequency of word
    median= year_sum.median()
    print("The median frequency of words in this year is", median)
     
    #Getting mean frequency of word
    mean= year_sum.mean()
    print("The mean frequency of words in this year is", int(mean))
    print("We have taken", str(year_plot.shape[0]), "speeches in", year)
    print()
    
    

for i in sorted(year):
    yearly_summary(i)
    yearly_plot(i)


# In[19]:


for i in sorted(year):
    years = date_frame['Date'] == i
    year_plot= date_frame[years]
    name= year_plot['Name'].unique().tolist()
    for h in name:
        person = year_plot['Name']== h
        person_data= year_plot[person]
        print(h, "has", person_data.shape[0], "speeches in", i + ".")
    print()


# In[2]:


#Test pairwise between Trump, Scott, and Theresa to see whether there's any association. If not, then can just do
#multiple regression, with their respective regression coefficients only including their unique effects.
#From here, https://www.theanalysisfactor.com/five-common-relationships-among-three-variables-in-a-statistical-model/
#we might be looking at either a covariate or a mediator (Trump affects everyone else and hence word over time)


# In[12]:


import pandas as pd
import matplotlib.pyplot as plt
df= pd.read_csv('C:/Users/Danny Chacko/Downloads/DTMlemma.csv')
def s(word):
    return word.strip()
df['Date']= pd.to_datetime(df['Date'].apply(s)) #set all dates to datetime object


# In[13]:


from datetime import datetime as dt
a= df.sort_values(by='Date')#sorting datetime object by date
a['Date'] = a['Date'].dt.strftime("%m") + a['Date'].dt.strftime("%Y")#isolates month and year before combining them
Trump_full = a[a['Name'] == 'Donald Trump']
t_police = Trump_full.filter(['police','Date'])
t_months = t_police['Date'].unique().tolist()
t_police[t_police['Date'] == t_months[0]]


# In[21]:


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


# In[22]:


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


# In[23]:


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


# In[26]:


#Correlation overall
get_ipython().run_line_magic('matplotlib', 'notebook')
from scipy.stats import spearmanr
#plt.plot(list(theresa_dict.values()), list(trump_dict.values()))
def compare_2_dicts(dict_1, dict_2, person1, person2):
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
        plt.xlabel(person1)
        plt.ylabel(person2)
        return plot_dict1, plot_dict2

list1, list2= compare_2_dicts(theresa_dict, trump_dict, "Theresa May", "Donald Trump")
list3, list4= compare_2_dicts(theresa_dict, scott_dict, "Theresa May", "Scott Morrison")
list5, list6= compare_2_dicts(trump_dict, scott_dict, "Donald Trump", "Scott Morrison")
print(spearmanr(list1, list2))
print(spearmanr(list3, list4))
print(spearmanr(list5, list6))


# In[27]:


#For Trump
import matplotlib.pyplot as plt
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


# In[28]:


#For Theresa
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


# In[29]:


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


# In[34]:


get_ipython().run_line_magic('matplotlib', 'notebook')
from scipy.stats import spearmanr
#plt.plot(list(theresa_dict.values()), list(trump_dict.values()))

#china_list1, china_list2= compare_2_dicts(theresa_china_dict, trump_china_dict, "Theresa May", "Donald Trump")
#china_list3, china_list4= compare_2_dicts(theresa_china_dict, scott_china_dict, "Theresa May", "Scott Morrison")
china_list5, china_list6= compare_2_dicts(trump_china_dict, scott_china_dict, "Donald Trump", "Scott Morrison")
#print(spearmanr(china_list1, china_list2))
#print(spearmanr(china_list3, china_list4))
print(spearmanr(china_list5, china_list6))


# In[ ]:





# In[ ]:




