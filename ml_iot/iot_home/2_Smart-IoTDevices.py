import pickle
import numpy as np
import pandas as pd
from datetime import datetime

# Load the models from the pickle files
with open('artifacts/ac_temperature_model.pkl', 'rb') as ac_model_file:
    regressor = pickle.load(ac_model_file)

with open('artifacts/light_on_off_model.pkl', 'rb') as light_model_file:
    classifier = pickle.load(light_model_file)

# Define the feature names for the input data
feature_names = ['outside_temperature', 'room_temperature', 'occupancy', 'hour', 'day_of_week']

# Function to get input from the user and make predictions
def get_user_input():
    print("Enter the following details:")
    outside_temp = int(input("Outside Temperature (°C): "))
    room_temp = int(input("Room Temperature (°C): "))
    occupancy = int(input("Room Occupied (1 for Yes, 0 for No): "))

    # Get current time or user input for time
    time_choice = input("Use current time? (y/n): ").strip().lower()
    if time_choice == 'y':
        current_time = datetime.now()
    else:
        time_str = input("Enter time (HH:MM, 24-hour format): ")
        current_time = datetime.strptime(time_str, '%H:%M')

    # Extract hour and day of the week
    hour = current_time.hour
    day_of_week = current_time.weekday()  # Monday=0, Sunday=6

    return pd.DataFrame([[outside_temp, room_temp, occupancy, hour, day_of_week]], columns=feature_names)


def predict_ac_and_light(features):
    # Predict the AC temperature
    ac_temp_pred = regressor.predict(features)
    
    # Predict whether the light should be on or off
    light_on_pred = classifier.predict(features)
    
    return ac_temp_pred[0], light_on_pred[0]


# Main function to run the script
if __name__ == "__main__":
    features = get_user_input()
    occupancy = features['occupancy'].iloc[0]
    ac_temp, light_on = predict_ac_and_light(features)

    if occupancy == 1: # if room occupied
        print(f"\nPredicted AC Temperature: {ac_temp} °C")
        if light_on == 1:
            print("Light Status: ON")
        else:
            print("Light Status: OFF")
    else:

        print("                   AC : OFF")	
        print("Empty room ---> ")	
        print("                Light : OFF")	
