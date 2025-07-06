import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import pickle
import os
import time

# Start timing
start_time = time.time()

# Load the dataset from separate CSV files
X_data = pd.read_csv('/Users/gopivardhan/Documents/CTML/house-price-prediciton/data/X_train.csv')
y_data = pd.read_csv('/Users/gopivardhan/Documents/CTML/house-price-prediciton/data/y_train.csv')

# If y is loaded as a DataFrame with a single column, convert to Series
if isinstance(y_data, pd.DataFrame) and y_data.shape[1] == 1:
    y_data = y_data.iloc[:, 0]

# Standardize features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X_data)

# Split data for training and validation
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y_data, test_size=0.2, random_state=42)

# Train linear regression model
training_start = time.time()
model = LinearRegression()
model.fit(X_train, y_train)
training_time = time.time() - training_start

# Make predictions
prediction_start = time.time()
y_train_pred = model.predict(X_train)
y_test_pred = model.predict(X_test)
prediction_time = time.time() - prediction_start

# Calculate metrics
# R-squared
train_r2 = r2_score(y_train, y_train_pred)
test_r2 = r2_score(y_test, y_test_pred)

# Mean Squared Error
train_mse = mean_squared_error(y_train, y_train_pred)
test_mse = mean_squared_error(y_test, y_test_pred)

# Mean Absolute Error
train_mae = mean_absolute_error(y_train, y_train_pred)
test_mae = mean_absolute_error(y_test, y_test_pred)

# Print metrics
print("Training metrics:")
print(f"R² score: {train_r2:.4f}")
print(f"MSE: {train_mse:.4f}")
print(f"MAE: {train_mae:.4f}")
print("\nTesting metrics:")
print(f"R² score: {test_r2:.4f}")
print(f"MSE: {test_mse:.4f}")
print(f"MAE: {test_mae:.4f}")

# Save model weights and metadata
weights = {
    'coefficients': model.coef_.tolist(),
    'intercept': model.intercept_,
    'feature_count': len(model.coef_)
}

# Save scaler for preprocessing new data
os.makedirs('model', exist_ok=True)
with open('model/regression_weights.pkl', 'wb') as f:
    pickle.dump(weights, f)
with open('model/scaler.pkl', 'wb') as f:
    pickle.dump(scaler, f)

# Also save as JSON for easier loading in C++
import json
with open('model/regression_weights.json', 'w') as f:
    json.dump(weights, f, indent=4)

# Calculate total execution time
total_time = time.time() - start_time

# Print timing information
print("\nExecution times:")
print(f"Training time: {training_time:.4f} seconds")
print(f"Prediction time: {prediction_time:.4f} seconds")
print(f"Total execution time: {total_time:.4f} seconds")

print("\nModel weights and scaler saved to 'model' directory")