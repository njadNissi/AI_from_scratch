import numpy as np
import pandas as pd
import random
from datetime import datetime, timedelta
import matplotlib.pyplot as plt

# Data generation parameters
days = 365
data_per_day = 24  # Data points per day (1 per hour)
n_samples = days * data_per_day

# Create a date range for a year
start_date = datetime(2023, 1, 1)
timestamps = [start_date + timedelta(hours=i) for i in range(n_samples)]

# Generate synthetic data
np.random.seed(42)
outside_temperature = np.round(np.random.normal(20, 10, n_samples)).astype(int)  # Simulating outside temp
occupancy = np.random.choice([0, 1], n_samples, p=[0.7, 0.3])  # 70% unoccupied, 30% occupied
ac_temperature = np.where(occupancy == 1, np.round(np.random.normal(22, 2, n_samples)).astype(int), np.nan)  # Set temp if occupied
room_temperature = outside_temperature + np.round(np.random.normal(2, 1, n_samples)).astype(int)  # Simulate room temp

# Light status based on occupancy and time of day
light_on = np.where((occupancy == 1) & ((np.array([d.hour for d in timestamps]) < 6) |
                                       (np.array([d.hour for d in timestamps]) > 18)), 1, 0)

# Create a DataFrame
df = pd.DataFrame({
    'timestamp': timestamps,
    'outside_temperature': outside_temperature,
    'room_temperature': room_temperature,
    'occupancy': occupancy,
    'ac_temperature': ac_temperature,
    'light_on': light_on
})

# Fill in missing AC temperatures when room is unoccupied
df['ac_temperature'].ffill(inplace=True)

# Display the first few rows of the dataset
print(df.tail(10))

# Save to CSV
df.to_csv('artifacts/synthetic_ac_light_data.csv', index=False)

