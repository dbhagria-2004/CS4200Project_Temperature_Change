import pandas as pd
import matplotlib.pyplot as plt

noaa = pd.read_csv("NOAA_GlobalData.csv", comment='#')

# Keep only 1924–2024
noaa = noaa[(noaa['Year'] >= 1924) & (noaa['Year'] <= 2024)]

print(noaa.head())
print(noaa.tail())

noaa = noaa.sort_values('Year')

noaa['Rolling_10yr'] = noaa['Anomaly'].rolling(window=10, center=True).mean()

print(noaa.head(15))
print(noaa.tail(15))
plt.figure(figsize=(12, 6))

# Actual annual anomaly
plt.plot(noaa['Year'], noaa['Anomaly'],
         color='lightgray', linewidth=1, label='Annual Temperature Anomaly')

# Smoothed trend line
plt.plot(noaa['Year'], noaa['Rolling_10yr'],
         color='darkred', linewidth=2.5, label='10-Year Rolling Average')

# Styling
plt.title("NOAA Global Temperature Anomalies (1924–2024)", fontsize=14, weight='bold')
plt.xlabel("Year", fontsize=12)
plt.ylabel("Temperature Anomaly (°C)", fontsize=12)
plt.grid(alpha=0.3)

plt.legend()
plt.tight_layout()
plt.show()
