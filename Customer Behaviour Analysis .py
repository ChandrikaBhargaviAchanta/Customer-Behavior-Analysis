#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Importing the Python Libraries
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Loading the Customer Data
data = pd.read_csv("downloads/ecommerce_customer_data.csv")
print(data.head())


# In[2]:


#Summary Statistics for numeric columns 
numeric_summary = data.describe()
print(numeric_summary)


# In[3]:


# Histogram for 'Age'
fig = px.histogram(data, x='Age', title ='Distribution of Age')
fig.show()


# In[4]:


# Barchart for Gender Distribution
gender_counts = data['Gender'].value_counts().reset_index()
gender_counts.columns = ['Gender', 'Count']
fig = px.bar(gender_counts, x='Gender', y='Count', title='Gender Distribution')
fig.show()


# In[5]:


# 'Product_Browsing_Time' vs 'Total_Pages_Viewed'
fig = px.scatter(data, x='Product_Browsing_Time', y='Total_Pages_Viewed',
                title='Product Browsing Time vs. Total Pages Viewed', 
                trendline='ols')
fig.show()


# In[6]:


#Average total pages viewed by Gender
#Grouped Analysis
gender_grouped = data.groupby('Gender')['Total_Pages_Viewed'].mean().reset_index()
gender_grouped.columns = ['Gender', 'Average_Total_Pages_Viewed']
fig =  px.bar(gender_grouped, x='Gender', y='Average_Total_Pages_Viewed', title='Average Total Pages Viewed by Gender')
fig.show()


# In[7]:


#Average total pages Viewed by Devices

devices_grouped = data.groupby('Device_Type')['Total_Pages_Viewed'].mean().reset_index()
devices_grouped.columns = ['Device_Type', 'Average_Total_Pages_Viewed']
fig = px.bar(devices_grouped, x='Device_Type', y='Average_Total_Pages_Viewed', title='Average Total Pages Viewed by Devices')
fig.show()


# In[8]:


#Calculating the Customer Life Time Value (CLTV) and visualizing segments based on CLTV
data['CLTV'] = (data['Total_Purchases'] * data['Total_Pages_Viewed']) / data['Age']

data['Segment'] = pd.cut(data['CLTV'], bins=[1, 2.5, 5, float('inf')],
                         labels=['Low Value', 'Medium Value', 'High Value'])

segment_counts = data['Segment'].value_counts().reset_index()
segment_counts.columns = ['Segment', 'Count']

# Create a bar chart to visualize the customer segments
fig = px.bar(segment_counts, x='Segment', y='Count', 
             title='Customer Segmentation by CLTV')
fig.update_xaxes(title='Segment')
fig.update_yaxes(title='Number of Customers')
fig.show()


# In[9]:


#Conversion Funnel of Customers 
# Funnel analysis
funnel_data = data[['Product_Browsing_Time', 'Items_Added_to_Cart', 'Total_Purchases']]
funnel_data = funnel_data.groupby(['Product_Browsing_Time', 'Items_Added_to_Cart']).sum().reset_index()

fig = px.funnel(funnel_data, x='Product_Browsing_Time', y='Items_Added_to_Cart', title='Conversion Funnel')
fig.show()


# In[10]:


#Calculate churn rate
data['Churned'] = data['Total_Purchases'] == 0

churn_rate = data['Churned'].mean()
print(churn_rate)


# In[ ]:




