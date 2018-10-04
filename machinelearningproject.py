
# coding: utf-8

# Machine Learning Project One
# BlackFriday Data Exploration

# In[1]:


import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


#Read files:
data = pd.read_csv("/Users/stellahrotich/Downloads/BlackFriday.csv")


# In[3]:


#check dataset 
data.head(10)


# In[4]:


#Looking at some basic statistics for numerical variables in the data 
data.describe()


# In[5]:


# The number of unique
print data.shape
    


# In[6]:


#Check Data Types For The columns
data.dtypes


# Data Cleaning
# 

# In[7]:


missing_values = data.isnull().sum().sort_values(ascending = False)
missing_values = missing_values[missing_values > 0]/data.shape[0]
missing_values*100


# In[8]:


data = data.fillna(0)


# In[9]:

#check data after  replacing the missing values

data.head(5)


# In[10]:


#unique values in Gender parameter

gender = np.unique(data['Gender'])
gender


# In[11]:

#replace the gender with numeric for easy analysis as numeric values 0 and 1

def numeric_gender(gender):
    if gender == 'M':
        return 1
    else:
        return 0
data['Gender'] = data['Gender'].apply(numeric_gender)


# In[12]:


age = np.unique(data['Age'])
age


# In[13]:


def numeric_age(age):
    if age == '0-17':
        return 0
    elif age == '18-25':
        return 18
    elif age == '26-35':
        return 26
    elif age == '36-45':
        return 45
    elif age == '46-50':
        return 46
    elif age == '51-55':
        return 51
    else:
        return 56
data['Age'] = data['Age'].apply(numeric_age)


# In[14]:


city_category = np.unique(data['City_Category'])
city_category


# In[15]:


def city_categories(city_category):
    if city_category == 'A':
        return 1
    elif city_category == 'B':
        return 2
    else:
        return 0
data['City_Category'] = data['City_Category'].apply(city_categories)


# In[16]:


city_stay = np.unique(data['Stay_In_Current_City_Years'])
city_stay


# In[17]:


def map_stay(stay):
        if stay == '4+':
            return 4
        else:
            return int(stay)
#             current_years = stay
#             current_years = current_years.astype(int)
#             return current_years
data['Stay_In_Current_City_Years'] = data['Stay_In_Current_City_Years'].apply(map_stay)


# In[18]:


#Drop the user_is and  product_id column
cols = ['User_ID','Product_ID']
data.drop(cols, inplace = True, axis =1)


# In[19]:


data.head(5)


# In[21]:


data[['Gender','Purchase']].groupby('Gender').mean().plot.bar()
sns.barplot('Gender', 'Purchase', data = data)
plt.show()


# How Age affects the Purchase Graph

# In[24]:


data[['Age','Purchase']].groupby('Age').mean().plot.bar()
sns.barplot('Age', 'Purchase', data = data)
plt.show()


# It doesnt matter the age on a Black Friday. All people are purchasing items because of the prices being cheap

# In[26]:


data[['City_Category','Purchase']].groupby('City_Category').mean().plot.bar()
sns.barplot('City_Category', 'Purchase', data = data)
plt.show()


# In[31]:


sns.boxplot('Age','Purchase', data = data)
plt.show()


# People in category 0 city tend to buy a little bit more ,it coulb be a bigger city

# No much deviation in Age groups purchases.No matter what age group you belong to, you are gonna make full use of your purchasing power on a Black Friday. Maybe, because everything is so damn cheap 

# In[32]:


corrmat = data.corr()
fig,ax = plt.subplots(figsize = (12,9))
sns.heatmap(corrmat, vmax=.8, square=True)


# Product_Category_1 has a negative correlation with Purchase.
# Maritial_Status and Age are strongly correlated. As Expected.
# Product_Category_3 has a strong correlation with Purchase. Maybe the products in this category were cheap. Let's chrun out some number related to this.

# That is the end of my refresher class YAAAAAAAAAAY!

# Thank you

# See you again soon

# Happy Learning
