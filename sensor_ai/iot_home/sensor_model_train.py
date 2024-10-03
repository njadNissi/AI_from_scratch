import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier
from sklearn.metrics import mean_squared_error, accuracy_score
import pickle


# Load the synthetic dataset
df = pd.read_csv('synthetic_ac_light_data.csv')

# Check for missing values in target columns (ac_temperature and light_on)
print("Checking for missing values...")
print(df[['ac_temperature', 'light_on']].isna().sum())

# Drop rows where target values are NaN
df = df.dropna(subset=['ac_temperature', 'light_on'])

# Convert timestamp to datetime format (if not already done)
df['timestamp'] = pd.to_datetime(df['timestamp'])

# Extract time-based features
df['hour'] = df['timestamp'].dt.hour  # Extract hour of the day (0-23)
df['day_of_week'] = df['timestamp'].dt.dayofweek  # Extract day of the week (0=Monday, 6=Sunday)

# Features (X) and labels (y)
X = df[['outside_temperature', 'room_temperature', 'occupancy', 'hour', 'day_of_week']]
y_temp = df['ac_temperature']  # For AC temperature prediction (regression)
y_light = df['light_on']  # For light on/off prediction (classification)

# Split data into training and test sets
X_train, X_test, y_temp_train, y_temp_test, y_light_train, y_light_test = train_test_split(X, y_temp, y_light, test_size=0.3, random_state=42)

# Train regression model for AC temperature
regressor = RandomForestRegressor(n_estimators=100, random_state=42)
regressor.fit(X_train, y_temp_train)

# Train classification model for light on/off
classifier = RandomForestClassifier(n_estimators=100, random_state=42)
classifier.fit(X_train, y_light_train)

# Predictions
y_temp_pred = regressor.predict(X_test)
y_light_pred = classifier.predict(X_test)

# Evaluate the models
mse_temp = mean_squared_error(y_temp_test, y_temp_pred)
accuracy_light = accuracy_score(y_light_test, y_light_pred)

print(f'AC Temperature Prediction MSE: {mse_temp:.2f}')
print(f'Light On/Off Prediction Accuracy: {accuracy_light:.2%}')

# Save the models using pickle
with open('ac_temperature_model.pkl', 'wb') as temp_model_file:
    pickle.dump(regressor, temp_model_file)

with open('light_on_off_model.pkl', 'wb') as light_model_file:
    pickle.dump(classifier, light_model_file)

print("Models saved successfully.")

