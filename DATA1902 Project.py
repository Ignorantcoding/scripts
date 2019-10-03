#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
df= pd.read_csv('C:/Users/Danny Chacko/Downloads/test1.csv')
def s(word):
    return word.strip()
df['Date']= df['Date'].apply(s)


# In[2]:


sums= df.sum(axis=0)
#To get columns with letter A or a in name, just do df.filter(regex= '[aA]'), same for no.s
#Automate column dropping is string late
sums_filter= sums.drop(['Date', 'Title', 'Name'])
#sums= sums.reset_index
# Looking at data overall
sums_filter= sums_filter.astype('int64') #convert from object to int64 type
total= sums_filter.sum(axis=0)
print("There are a total of", total, "values in our dataset.")

word= sums_filter.filter(regex= '^[A-Za-z]+$', axis=0)
print("The most used word is", "'" + word.idxmax() +"'.")

number= sums_filter.filter(regex= '[0-9]', axis=0)
print("The most used number is", number.idxmax() + ".")


# In[21]:


sums_filter= sums_filter.sort_values(ascending= False)
top_100= sums_filter[:25]/total
import matplotlib.pyplot as plt
top_100.plot(kind="bar", figsize=(20,10))


# In[57]:


import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'notebook')
def filter_by_name(names_list):
    #h= 1
    for i in names_list:
        name = df['Name'] == str(i)
        name_data = df[name]
        name_sum = name_data.sum(axis=0)
        name_sum = name_sum.drop(['Date', 'Title', 'Name'])
        name_sum = name_sum.astype('int64') #convert from object to int64 type
        name_sum = name_sum.sort_values(ascending= False)
        top25= name_sum[:25]
        
        fig = plt.figure(figsize=plt.figaspect(1.))
        #ax= fig.add_subplot(2, 2, h)
        top25.plot(kind="bar")
        plt.title(str(i))
        plt.xlabel('Top 25 Words')
        plt.ylabel('Frequencies')
        
        #h+=1
        print(name_sum['police'])
        
def name_summary(names):
    for i in names:
        name = df['Name'] == str(i)
        name_data = df[name]
        name_sum = name_data.sum(axis=0)
        name_sum = name_sum.drop(['Date', 'Title', 'Name'])
        name_sum = name_sum.astype('int64')
        name_sum= name_sum[name_sum != 0] # To remove rows that have 0 in it

        #Getting total no.
        total= name_sum.sum(axis=0)   
        distinct= name_sum.count()
        print("There are a total of", total, "values and", distinct, "distinct values for", str(i) + ".")
        
        #Distinct words
        words= name_sum.filter(regex= '^[A-Za-z]+$', axis=0)
        words_distinct= words.count()
        print(str(i) + " has used", words_distinct, "distinct words altogether.")
        
        #print("Most common word for " + str(i) + " is" + " '" + name_sum.idxmax() + "'" + ", occuring", name_sum.max(), "times.")

        #Getting median frequency of word
        median= name_sum.median()
        print("The median frequemcy of words for " + str(i) + " is " + str(median))

        #Getting mean frequency of word
        mean= int(name_sum.mean())
        print("The mean frequemcy of words for " + str(i) + " is " + str(mean))
        print() 
    
names= df['Name'].unique().tolist()
filter_by_name(names)
name_summary(names)


# In[48]:


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
    print("The median frequemcy of words in this year is", median)
     
    #Getting mean frequency of word
    mean= year_sum.mean()
    print("The mean frequemcy of words in this year is", int(mean))
    print()
    
    

    
for i in sorted(year):
    yearly_summary(i)
    yearly_plot(i)


# In[35]:


print(date_frame)


# In[ ]:




