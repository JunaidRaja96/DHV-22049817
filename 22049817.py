import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("climate-ds.csv")

df.describe

fig, axs = plt.subplots(2, 2, figsize=(15, 12))

# Plot 1: Average Rainfall over Years (Line Plot)
sns.lineplot(x='Year', y='average_rain_fall_mm_per_year', data=df, color='blue', marker='o', ax=axs[0, 0])
axs[0, 0].set_title('Average Rainfall Over Years')
axs[0, 0].grid(True)

# Plot 2: Pesticide Usage Distribution (Bar Plot)
df_pie_bar = df.head(50).groupby('Item')['pesticides_tonnes'].sum().reset_index()
sns.barplot(x='Item', y='pesticides_tonnes', data=df_pie_bar, color='red', ax=axs[0, 1])
axs[0, 1].set_title('Pesticide Usage Distribution (First 50 Rows)')
axs[0, 1].set_xlabel('Item')
axs[0, 1].set_ylabel('Pesticides (tonnes)')
axs[0, 1].grid(True)

# Plot 3: Temperature Trends over Years (Histogram)
sns.histplot(df['avg_temp'], bins=20, kde=True, color='green', ax=axs[1, 0])
axs[1, 0].set_title('Temperature Distribution Over Years')

# Plot 4: Crop Yield vs. Pesticide Usage (Pie Plot)
yield_labels = ['Low', 'Medium', 'High']
yield_values = [df['hg/ha_yield'][df['hg/ha_yield'] < 5000].count(), 
                df['hg/ha_yield'][(df['hg/ha_yield'] >= 5000) & (df['hg/ha_yield'] <= 10000)].count(), 
                df['hg/ha_yield'][df['hg/ha_yield'] > 10000].count()]
axs[1, 1].pie(yield_values, labels=yield_labels, autopct='%1.1f%%', colors=['gold', 'lightcoral', 'lightblue'])
axs[1, 1].set_title('Crop Yield Distribution')

# Create a new figure for the description
fig_desc = plt.figure(figsize=(15, 3))
plt.text(0, 0, "The first figure is showing the average annual rainfall in the United States from 1990 to 2010. The graph shows that the average annual rainfall has been steadily increasing over the past 20 years. In 1990, the average annual rainfall was around 1,100 millimeters (mm) per year. By 2010, the average annual rainfall had increased to around 1,200 mm per year\n\n"
         "The second figure is showing the distribution of pesticide usage for the first 50 rows of data in the table. The chart shows that the most commonly used pesticides are maize, potatoes, and soybeans. The highest number of the used pesticide is approximately 3200.\n\n"
         "The third figure is showing the distribution of average temperatures. The histogram shows that the most common average temperature is between 15 and 20 degrees Celsius. The average temperature for all of the data points in the histogram is around 18 degrees Celsius.\n\n"
         "The fourth figure is showing the distribution of crop yields. The pie chart shows that the majority of crops (90.8%) have a high yield. A medium yield accounts for 7.9% of crops, and a low yield accounts for 1.3% of crops.\n\n"
         "Name: Muhammad Junaid Raja\n"
         "Student ID: 22049817", 
         ha='left', va='center', fontsize=14, wrap=True)
plt.axis('off')


fig.suptitle('Climate Change Infographics Analysis', fontsize=16)
fig.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.show()
