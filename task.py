import requests
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# OpenWeatherMap API setup
API_KEY = "YOUR_API_KEY"  # Replace with your actual API key
CITY = "London"
URL = f"https://api.openweathermap.org/data/2.5/forecast?q={CITY}&appid={API_KEY}&units=metric"

# Fetch weather data
response = requests.get(URL)
if response.status_code == 200:
    data = response.json()
else:
    print("Failed to fetch data from OpenWeatherMap API.")
    exit()

# Extract relevant data
dates = []
temperatures = []
humidity = []

for entry in data['list']:
    dates.append(entry['dt_txt'])
    temperatures.append(entry['main']['temp'])
    humidity.append(entry['main']['humidity'])

# Create a DataFrame
df = pd.DataFrame({
    'Date': pd.to_datetime(dates),
    'Temperature (C)': temperatures,
    'Humidity (%)': humidity
})

# Plot Temperature Trend using Matplotlib
plt.figure(figsize=(12, 6))
plt.plot(df['Date'], df['Temperature (C)'], marker='o', color='orange')
plt.title(f'Temperature Trend in {CITY}')
plt.xlabel('Date')
plt.ylabel('Temperature (C)')
plt.xticks(rotation=45)
plt.grid(True)
plt.show()

# Plot Temperature and Humidity using Seaborn
plt.figure(figsize=(14, 7))
sns.lineplot(data=df, x='Date', y='Temperature (C)', label='Temperature (C)', color='red')
sns.lineplot(data=df, x='Date', y='Humidity (%)', label='Humidity (%)', color='blue')
plt.title(f'Temperature and Humidity Trends in {CITY}')
plt.xlabel('Date')
plt.xticks(rotation=45)
plt.legend()
plt.show()

print("Data visualization complete.")
