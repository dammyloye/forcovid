import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
df = pd.read_csv('owid-covid-data.csv')

# Explore data
print(df.columns)
print(df.head())
print(df.isnull().sum())

# Clean data
df = df.dropna(subset=['date', 'location'])
df['date'] = pd.to_datetime(df['date'])

# Filter countries
countries = ['Kenya', 'USA', 'India']
df = df[df['location'].isin(countries)]

# Plot total cases over time
plt.figure(figsize=(10, 6))
for country in countries:
    df_country = df[df['location'] == country]
    plt.plot(df_country['date'], df_country['total_cases'], label=country)
plt.xlabel('Date')
plt.ylabel('Total Cases')
plt.title('Total Cases Over Time')
plt.legend()
plt.show()

# Plot total deaths over time
plt.figure(figsize=(10, 6))
for country in countries:
    df_country = df[df['location'] == country]
    plt.plot(df_country['date'], df_country['total_deaths'], label=country)
plt.xlabel('Date')
plt.ylabel('Total Deaths')
plt.title('Total Deaths Over Time')
plt.legend()
plt.show()

# Calculate death rate
df['death_rate'] = df['total_deaths'] / df['total_cases']

# Plot death rate over time
plt.figure(figsize=(10, 6))
for country in countries:
    df_country = df[df['location'] == country]
    plt.plot(df_country['date'], df_country['death_rate'], label=country)
plt.xlabel
