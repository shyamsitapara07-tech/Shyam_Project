import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os


df=pd.read_csv("Weather_Data.csv")
#print(df)

df['Date'] = pd.to_datetime(df['Date'])
df.fillna({
    "Precipitation": 0,
    "WindSpeed": df["WindSpeed"].mean(),
    "Humidity": df["Humidity"].mean()
}, inplace=True)

df['month'] = df['Date'].dt.month
df['day'] = df['Date'].dt.day

avg_temp = df['Temperature'].mean()
avg_humidity = df['Humidity'].mean()
#print(f"Average Temperature: {avg_temp:.2f} c")
#print(f"Average Humidity: {avg_humidity:.2f} %")


condition_count = df["Condition"].value_counts()
#print("Weather Condition Counts:")
#print(condition_count)

#1. Temperature trend
plt.figure(figsize=(10, 5))
plt.plot(df['Date'], df['Temperature'], marker='o')
plt.title('Daily Temperature Trend')
plt.xlabel('Date')
plt.ylabel('Temperature (°C)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('temperature_trend.png')
os.startfile('temperature_trend.png')
plt.show()

#2. Humidity trend
plt.figure(figsize=(10, 5))
plt.plot(df['Date'], df['Humidity'], marker='o', color='blue')
plt.title('Daily Humidity Trend')
plt.xlabel('Date')
plt.ylabel('Humidity (%)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('humidity_trend.png')
os.startfile('humidity_trend.png')
plt.show()

#3. Condition frequency
plt.figure(figsize=(8, 5))
sns.countplot(x='Condition', data=df, hue='Condition', palette='Set2', legend=False)
plt.title('Weather Condition Frequency')
plt.xlabel('Condition')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('condition_frequency.png')
os.startfile('condition_frequency.png')
plt.show()

#4. Temperature vs Humidity (scatter plot)
plt.figure(figsize=(10, 5))
plt.scatter(df['Temperature'], df['Humidity'], alpha=0.5, color='green')
plt.title('Temperature vs Humidity')
plt.xlabel('Temperature (°C)')
plt.ylabel('Humidity (%)')
plt.tight_layout()
plt.savefig('temp_vs_humidity.png')
os.startfile('temp_vs_humidity.png')
plt.show()

#5. Corelation heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(df[['Temperature', 'Humidity', 'WindSpeed', 'Precipitation']].corr(), annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.tight_layout()
plt.savefig('correlation_heatmap.png')
os.startfile('correlation_heatmap.png')
plt.show()

#6. Monthly average temperature
monthly_avg_temp = df.groupby('month')['Temperature'].mean()
plt.figure(figsize=(10, 5))
monthly_avg_temp.plot(kind='bar', color='orange')
plt.title('Average Temperature by Month')
plt.xlabel('Month')
plt.ylabel('Average Temperature (°C)')
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig('monthly_avg_temp.png')
os.startfile('monthly_avg_temp.png')
plt.show()


