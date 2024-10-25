import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import root_mean_squared_error as mse
import pickle

# Load your dataset
data = pd.read_csv('artifacts/nfFormulaData.csv')

# Prepare features and target variable
y = data['y']  # Replace with your features
X = data.drop('y', axis=1)

print(X.head(), y.head())

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create and train the Linear Regression model
model = LinearRegression()
model.fit(X_train, y_train)
# Print weights and bias
print("Weights:", model.coef_)
print("Bias:", model.intercept_)

# Make predictions
predictions = model.predict(X_test)

m2e = mse(y_test, predictions)
print(f'Mean Squared Error: {m2e:.2f}')
print(predictions)


# Open a file in write binary mode ('wb') for saving the model
with open('artifacts/nfFormulaModel.pkl', 'wb') as f:
  # Use pickle.dump to serialize the model and write it to the file
  pickle.dump(model, f)