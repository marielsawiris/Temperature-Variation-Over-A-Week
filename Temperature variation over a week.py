import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv('1_Daily_minimum_temps.csv')
data['Date'] = pd.to_datetime(data['Date'])
week_data = data.iloc[0:7]

plt.figure(figsize=(8, 5))
plt.plot(week_data['Date'], week_data['Temp'], marker='o', linestyle='-', color='black')
plt.title('Temperature Variation Over a Week')
plt.xlabel('Date')
plt.ylabel('Temperature (°C)')
plt.xticks(rotation=45)
plt.show()