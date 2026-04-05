# Zomato Dataset Analysis Project

# step-1: Importing the libraries

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# step-2: Importing the dataset

df=pd.read_csv("Zomato_data.csv")
"""
print(df)
print(df.head())
"""
# Type of Restaurant

sns.countplot(x=df['listed_in(type)'])
plt.xlabel('Type of Restaurant',fontsize=14)
plt.ylabel('Count',fontsize=14)
plt.title('Total Restaurants',fontsize=20)
plt.savefig('Total_Restaurants.png')
plt.show()

grouped_data = df.groupby('listed_in(type)')['votes'].sum()
result = pd.DataFrame({'votes' : grouped_data})
plt.plot(result, c="#3B00C6",marker='o')
plt.xlabel('Type of Restaurant',fontsize=14)
plt.ylabel('Votes',fontsize=14)
plt.title('Votes for each type of restaurant',fontsize=20)
plt.savefig('Votes_by_Restaurant_Type.png')
plt.show()  

plt.hist(df['rate'], bins=5,color="#F975B0", edgecolor="#000000")
plt.title('Rating Distribution',fontsize=20)
plt.xlabel('Rating',fontsize=14)
plt.ylabel('Number of Restaurants',fontsize=14)
plt.savefig('Rating_Distribution.png')
plt.show()

cople_data=df['approx_cost(for two people)']
sns.countplot(x=cople_data)
plt.title('Cost for two people',fontsize=20)
plt.xlabel('Cost for two people',fontsize=14)
plt.ylabel('Count',fontsize=14)
plt.savefig('Cost_for_Two_People.png')
plt.show()

plt.figure(figsize=(10,6))
sns.boxplot(x = 'online_order', y = 'rate', data = df)
plt.title('Box Plot of Online Order vs Rate',fontsize=20)
plt.xlabel('Online Order',fontsize=14)
plt.ylabel('Rate',fontsize=14)
plt.savefig('Online_Order_vs_Rate.png')
plt.show()

pivot_table = df.pivot_table(index='listed_in(type)', columns='online_order', aggfunc='size', fill_value=0)
sns.heatmap(pivot_table, annot=True, fmt='d', cmap='YlGnBu')
plt.title("Heatmap", fontsize=20)
plt.xlabel("Online Order", fontsize=14)
plt.ylabel("Type of Restaurant", fontsize=14)
plt.savefig('Online_Order_vs_Restaurant_Type.png')
plt.show()
