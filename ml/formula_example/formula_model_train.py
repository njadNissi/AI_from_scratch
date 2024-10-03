import everywhereml as eml
import pandas as pd
from sklearn.model_selection import train_test_split
from everywhereml
from sklearn.metrics import mean_squared_error

# Load your dataset
data = pd.read_csv('3fFormulaRegressor.csv')

# Prepare features and target variable
X = data[['x1', 'x2', 'x3']]  # Replace with your features
y = data['Y']  # Replace with your target variable

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create and train the Linear Regression model
model = eml # LinearRegression()
model.fit(X_train, y_train)

# Make predictions
predictions = model.predict(X_test)

mse = mean_squared_error(y_test, predictions)
print(f'Mean Squared Error: {mse:.2f}')
print(predictions)


# save  model for aduino
name = "3fFormulaRegressor"
with open(f'{name}.h', 'w') as f:
  f.write(model.to_arduino(instance_name=name))